import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
import os.path
from django.conf import settings
from bs4 import BeautifulSoup
import requests
import datetime
import nltk
import csv

from core.models import Course

# FILE PATHS

my_path = os.path.abspath(os.path.dirname(__file__))
springboard_scrape_path = os.path.join(settings.BASE_DIR, "data/datasets/springboard_scrape.csv")
springboard_clean_path = os.path.join(settings.BASE_DIR, "data/datasets/springboard_clean.csv")
springboard_mlb_path = os.path.join(settings.BASE_DIR, "data/datasets/springboard_mlb.csv")
stopwords_path = os.path.join(settings.BASE_DIR, "data/datasets/stopwords.txt")


## WEBCRAWLER ##########################################################################################################

def my_tokenizer(s):
    """Word Tokenization"""
    # Stopwords file:
    stopwords = set(w.rstrip() for w in open(stopwords_path))
    s = s.lower()
    tokens = nltk.tokenize.word_tokenize(s)
    tokens = [t for t in tokens if len(t) > 2]
    tokens = [t for t in tokens if t not in stopwords]
    return tokens


def data_extractor():
    """Dataset Extraction"""

    # Load WebPage
    source = requests.get('http://springboardcourses.ie/results?keywords=&perPage=500').text

    # Pass source to beautifulsoup:
    soup = BeautifulSoup(source, 'lxml')

    # CSV file
    csv_file = open(springboard_scrape_path, 'w')

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(
        ['title', 'provider', 'award', 'ects_credits', 'mode', 'deadline', 'start_date', 'end_date', 'nfq', 'ote_flag',
         'skill_area', 'link'])

    for course_div in soup.find_all('div', class_="panel panel-primary"):

        try:
            # Course Title
            title_div = course_div.find('div', class_="panel-heading").h3.text

            # First Content Row

            first_row = course_div.find('div', class_="panel-body")

            # Provider:
            provider = first_row.find('div', class_="col-md-12").p
            provider = str(provider).split('</strong>')[1]
            provider = provider.split('<')[0]

            # Award:
            award = first_row.find('div', class_="col-md-5").p
            award = str(award).split('</strong>')[1]
            award = award.split('<')[0]

            # ECTS credits:
            credits = first_row.find('div', class_="col-md-3")
            credits = str(credits).split('</strong> ')[1]
            credits = credits.split('<')[0]

            # Second Content Row

            second_row = first_row.find_all('div', "row")[2]

            # Mode:
            mode = second_row.find('div', class_="col-md-5")
            mode = str(mode).split('</strong> ')[1]
            mode = mode.split('<')[0]

            # Application Deadline:
            deadline = second_row.find('div', class_="col-md-4")
            deadline = str(deadline).split('</strong>')[1]
            deadline = deadline.split('<')[0]

            # Start Date
            start_date = second_row.find('div', class_="col-md-3")
            start_date = str(start_date).split('</strong>')[1]
            start_date = start_date.split('<')[0]

            # End Date
            end_date = second_row.find('div', class_="col-md-3")
            end_date = str(end_date).split('</strong>')[2]
            end_date = end_date.replace(" ", "")
            end_date = end_date.split('<')[0]

            # Bottom Content Row

            third_row = first_row.find('div', "row margin-bottom-0")

            # NFQ
            nfq = third_row.find('div', class_="col-md-5").p
            nfq = str(nfq).split('</strong>')[1]
            nfq = nfq.split('<')[0]

            # Open to those in employment
            ote_flag = third_row.find('div', class_="col-md-4").p
            ote_flag = str(ote_flag).split('</strong>')[1]
            ote_flag = ote_flag.split('<')[0]

            # Skills area
            skill_list = third_row.find('div', class_="col-md-3")
            skill_list = str(skill_list).split('</strong>')[1]
            skill_list = skill_list.split('<')[0]
            skill_list = my_tokenizer(skill_list)

            # Course Link
            link = course_div.find('a')
            link = link.get('href')

        except Exception as e:

            title_div = None
            provider = None
            award = None
            credits = None
            mode = None
            deadline = None
            start_date = None
            end_date = None
            nfq = None
            ote_flag = None
            skill_list = None
            link = None

        csv_writer.writerow(
            [title_div, provider, award, credits, mode, deadline, start_date, end_date, nfq, ote_flag, skill_list,
             link])

    csv_file.close()


## DATA CLEANING #######################################################################################################


def date_cleaner(dataset, column, datetime_format):
    """Clean DataTime columns helper function"""
    clean_date = []
    for date in dataset[column]:
        if len(date) < 8:
            date = '01/' + date
        else:
            date = date
        date = datetime.datetime.strptime(date, datetime_format)
        date = date.date()
        clean_date.append(date)

    return clean_date


def dataset_preprocessing():
    """dataset cleaning function"""
    dataset = pd.read_csv(springboard_scrape_path)
    dataset = dataset.dropna()
    datetime_format = '%d/%m/%Y'

    # Cleaning Date Fields
    dataset['deadline'] = date_cleaner(dataset, 'deadline', datetime_format)
    dataset['start_date'] = date_cleaner(dataset, 'start_date', datetime_format)
    dataset['end_date'] = date_cleaner(dataset, 'end_date', datetime_format)
    # OTE_FLAG replace with 0-1
    dataset['ote_flag'] = dataset['ote_flag'].map({'Yes': 1, 'No': 0})

    # Skill area column cleaning
    clean_skills = []
    for element in dataset['skill_area']:
        element = element.replace("[", "")
        element = element.replace("]", "")
        element = element.replace("'", "")
        element = element.strip()
        clean_skills.append(element)

    dataset['skills'] = clean_skills

    # Print to CSV
    dataset.to_csv(springboard_clean_path, index=False)


def data_visualization():
    dataset_raw = pd.read_csv(springboard_scrape_path)
    dataset_clean = pd.read_csv(springboard_clean_path)

    dataset_raw = dataset_raw.dropna()  # remove empty rows

    dataset_raw_head = dataset_raw.head(10)  # first 10 rows
    dataset_clean_head = dataset_clean.head(10)

    dates_raw = dataset_raw.iloc[:10, [5, 6, 7]]
    dates_clean = dataset_clean.iloc[:10, [5, 6, 7]]

    ote_raw = dataset_raw.iloc[:10, 9:10]
    ote_clean = dataset_clean.iloc[:10, 9:10]

    skill_raw = dataset_raw.iloc[:10, 10:11]

    data_dict = {"dataset_raw_head": dataset_raw_head.to_html(),
                 "dataset_clean_head": dataset_clean_head.to_html(),
                 "dates_raw": dates_raw.to_html(),
                 "dates_clean": dates_clean.to_html(),
                 "ote_raw": ote_raw.to_html(),
                 "ote_clean": ote_clean.to_html(),
                 "skill_raw": skill_raw.to_html(),
                 }

    return data_dict


def mlb_vizualization():
    dataset_mlb = pd.read_csv(springboard_mlb_path)
    skill_clean = dataset_mlb.iloc[:10, :]


    return skill_clean


## MLB #############################################################################################################

def data_binarizer():
    dataset = pd.read_csv(springboard_clean_path)
    dataset = dataset.iloc[:, 10:11]

    clean_skills = []
    for element in dataset['skill_area']:
        element = element.replace("[", "")
        element = element.replace("]", "")
        element = element.replace("'", "")
        element = element.strip()
        clean_skills.append(element)

    df_skills = pd.DataFrame()
    df_skills['skills'] = clean_skills

    skill_list = []
    for element in df_skills['skills']:
        skills = element.split(',')
        skill_list.append(skills)

    skill_area = pd.DataFrame()
    skill_area['skills_list'] = skill_list

    ### Skill Area featurization

    mlb = MultiLabelBinarizer()

    new_array = mlb.fit_transform(skill_area['skills_list'])
    skill_classes = list(mlb.classes_)
    df_skills_transformed = pd.DataFrame(data=new_array, columns=skill_classes)
    df_skills_transformed.to_csv(springboard_mlb_path, index=False)


## DATABASE ############################################################################################################

def database_upload():
    courses = Course.objects.all()
    courses.delete()
    with open(springboard_clean_path) as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                _, created = Course.objects.get_or_create(title=row[0], provider=row[1], award=row[2],
                                                          ects_credits=row[3], mode=row[4], deadline=row[5],
                                                          start_date=row[6], end_date=row[7], nfq=row[8],
                                                          ote_flag=row[9], link=row[11], skills=row[12]
                                                          )
            except:
                pass
