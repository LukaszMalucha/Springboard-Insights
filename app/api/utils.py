import datetime
import os
import urllib
from http.client import IncompleteRead
from urllib.request import Request

import bs4 as bs
import pandas as pd
from django.conf import settings

from core.models import CourseModel

# FILE PATHS

my_path = os.path.abspath(os.path.dirname(__file__))
stopwords_path = os.path.join(settings.BASE_DIR, "api/datasets/stopwords.txt")


# Date Cleaner

def date_cleaner(date):
    """Clean DataTime columns helper function"""
    datetime_format = "%d/%m/%Y"
    if len(date) < 8:
        date = "01/" + date
    else:
        date = date
    clean_date = datetime.datetime.strptime(date, datetime_format).strftime("%Y/%m/%d")
    return clean_date


# WEBCRAWLER

def data_extractor():
    """Dataset Extraction"""

    # Load WebPage
    try:
        req = urllib.request.Request(
            "http://springboardcourses.ie/results?keywords=&perPage=500",
            data=None,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
            })
    except IncompleteRead:
        req = urllib.request.Request(
            "http://springboardcourses.ie/results?keywords=&perPage=500",
            data=None,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
            })

    f = urllib.request.urlopen(req)
    soup = bs.BeautifulSoup(f, "lxml")

    courses = []

    for course_div in soup.find_all("div", class_="panel panel-primary"):

        try:
            # Course Title
            title_div = course_div.find("div", class_="panel-heading").h3.text
            title_div = title_div.strip()
            title_div = title_div.replace("  ", "")

        except Exception as e:
            title_div = None

        try:
            # First Content Row

            first_row = course_div.find("div", class_="panel-body")

            # Provider:
            provider = first_row.find("div", class_="col-md-12").p
            provider = str(provider).split("</strong>")[1]
            provider = provider.split("<")[0]

            # Award:
            award = first_row.find("div", class_="col-md-5").p
            award = str(award).split("</strong>")[1]
            award = award.split("<")[0]

            # Delivery Method:
            delivery = first_row.find("div", class_="col-md-4").p
            delivery = str(delivery).split("</strong>")[1]
            delivery = delivery.split("<")[0]

            # ECTS credits:
            ects_credits = first_row.find("div", class_="col-md-3")
            ects_credits = str(ects_credits).split("</strong> ")[1]
            ects_credits = ects_credits.split("<")[0]

            # Second Content Row
            second_row = first_row.find_all("div", "row")[2]

            # Mode:
            mode = second_row.find("div", class_="col-md-5")
            mode = str(mode).split("</strong> ")[1]
            mode = mode.split("<")[0]

            # Application Deadline:
            deadline = second_row.find("div", class_="col-md-4")
            deadline = str(deadline).split("</strong>")[1]
            deadline = deadline.split("<")[0]
            deadline = date_cleaner(deadline)

            # Start Date
            start_date = second_row.find("div", class_="col-md-3")
            start_date = str(start_date).split("</strong>")[1]
            start_date = start_date.split("<")[0]
            start_date = date_cleaner(start_date)

            # End Date
            end_date = second_row.find("div", class_="col-md-3")
            end_date = str(end_date).split("</strong>")[2]
            end_date = end_date.replace(" ", "")
            end_date = end_date.split("<")[0]
            end_date = date_cleaner(end_date)

            # Bottom Content Row
            third_row = first_row.find("div", "row margin-bottom-0")

            # NFQ
            nfq = third_row.find("div", class_="col-md-5").p
            nfq = str(nfq).split("</strong>")[1]
            nfq = nfq.split("<")[0]
            nfq = nfq.replace("Level ", "")

            # Open to those in employment
            ote_flag = third_row.find("div", class_="col-md-4").p
            ote_flag = str(ote_flag).split("</strong>")[1]
            ote_flag = ote_flag.split("<")[0]

            # Skills area
            skill_list = third_row.find("div", class_="col-md-3")
            skill_list = str(skill_list).split("</strong>")[1]
            skill_list = skill_list.split("<")[0]
            skill_list = skill_list.lower()

            # Course Link
            link = course_div.find("a")
            link = link.get("href")


        except Exception as e:
            provider = None
            award = None
            delivery = None
            ects_credits = None
            mode = None
            deadline = None
            start_date = None
            end_date = None
            nfq = None
            ote_flag = None
            skill_list = None
            link = None

        courses.append({"title": title_div, "provider": provider, "award": award,
                        "ects_credits": ects_credits, "mode": mode, "deadline": deadline,
                        "start_date": start_date, "end_date": end_date, "nfq": nfq,
                        "ote_flag": ote_flag, "skill_list": skill_list, "link": link, "delivery": delivery})

    return courses


def database_upload(course_list):
    courses = Course.objects.all()
    courses.delete()

    for row in course_list:
        try:
            _, created = Course.objects.get_or_create(title=row['title'], provider=row['provider'], award=row['award'],
                                                      ects_credits=row['ects_credits'], mode=row['mode'],
                                                      deadline=row['deadline'], start_date=row['start_date'],
                                                      end_date=row['end_date'], nfq=row['nfq'],
                                                      ote_flag=row['ote_flag'], link=row['link'],
                                                      skills=row['skill_list'], delivery=row['delivery']
                                                      )
        except:
            pass


def statistical_data():
    dataset = pd.DataFrame(list(Course.objects.all().values()))

    if len(dataset.index) > 0:

        # top providers
        occurence = dataset["provider"].value_counts()[:6]
        top_providers_dict = occurence.to_dict()

        # Delivery mode
        dataset["less_than_50"] = dataset["ects_credits"].apply(
            lambda x: "below 50 C" if int(x) < 50 else "over 50 C")
        less_than_50_values = dataset["less_than_50"].value_counts()
        lt50_dict = less_than_50_values.to_dict()

        # partime/ fulltime
        mode_values = dataset["mode"].value_counts()
        mode_dict = mode_values.to_dict()

        # NFQ
        nfq_values = dataset["nfq"].value_counts()
        nfq_dict = nfq_values.to_dict()

        # Top popular categories
        category_values = dataset["skills"].value_counts()[:6]
        category_dict = category_values.to_dict()

        stats_dict = {"top_providers_dict": top_providers_dict,
                      "lt50_dict": lt50_dict,
                      "nfq_dict": nfq_dict,
                      "mode_dict": mode_dict,
                      "category_dict": category_dict
                      }
    else:
        stats_dict = {}

    return stats_dict


def fastest_diploma(queryset):
    dataset = pd.DataFrame(list(queryset.values()))
    if len(dataset.index) > 0:
        diplomas = ["Diploma", "diploma"]
        dataset["diploma"] = dataset["title"].apply(lambda x: 1 if any(w in x for w in diplomas) else 0)
        dataset_diplomas = dataset[(dataset["diploma"] == 1)]

        # top 12 shortest diplomas
        if len(dataset_diplomas.index) > 0:
            dataset_diplomas["start_date"] = pd.to_datetime(dataset_diplomas["start_date"]).dt.date
            dataset_diplomas["end_date"] = pd.to_datetime(dataset_diplomas["end_date"]).dt.date

            dataset_diplomas["duration"] = (dataset_diplomas["end_date"] - dataset_diplomas["start_date"]).astype(
                "timedelta64[D]").astype(int)
            dataset_diplomas = dataset_diplomas.sort_values(["duration"])[:12]
            dataset_diplomas_list = dataset_diplomas.values.tolist()
        else:
            dataset_diplomas_list = []
    else:
        dataset_diplomas_list = []

    return dataset_diplomas_list


def fastest_bachelor(queryset):
    dataset = pd.DataFrame(list(queryset.values()))
    bachelors = ["Bachelors", "Bachelor", "bachelor", "bsc", "Bsc"]
    dataset["bachelor"] = dataset["title"].apply(lambda x: 1 if any(w in x for w in bachelors) else 0)
    dataset_bachelors = dataset[(dataset["bachelor"] == 1)]

    # top 12 shortest diplomas
    if len(dataset_bachelors.index) > 0:
        dataset_bachelors["start_date"] = pd.to_datetime(dataset_bachelors["start_date"]).dt.date
        dataset_bachelors["end_date"] = pd.to_datetime(dataset_bachelors["end_date"]).dt.date

        dataset_bachelors["duration"] = (dataset_bachelors["end_date"] - dataset_bachelors["start_date"]).astype(
            "timedelta64[D]").astype(int)
        dataset_bachelors = dataset_bachelors.sort_values(["duration"])[:12]
        dataset_bachelors_list = dataset_bachelors.values.tolist()
    else:
        dataset_bachelors_list = []

    return dataset_bachelors_list


def online_courses(queryset):
    dataset = pd.DataFrame(list(queryset.values()))
    dataset["online"] = dataset["delivery"].apply(lambda x: 1 if x == "Online" else 0)
    dataset_online = dataset[(dataset["online"] == 1)]
    if len(dataset_online.index) > 0:
        dataset_online["start_date"] = pd.to_datetime(dataset_online["start_date"]).dt.date
        dataset_online["end_date"] = pd.to_datetime(dataset_online["end_date"]).dt.date

        dataset_online["duration"] = (dataset_online["end_date"] - dataset_online["start_date"]).astype(
            "timedelta64[D]").astype(int)
        dataset_online_list = dataset_online.values.tolist()
    else:
        dataset_online_list = []

    return dataset_online_list
