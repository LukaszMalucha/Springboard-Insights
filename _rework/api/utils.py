import csv
import os
import bs4 as bs
from urllib.request import Request
import urllib
import nltk
import requests
from bs4 import BeautifulSoup
from django.conf import settings

# FILE PATHS

my_path = os.path.abspath(os.path.dirname(__file__))
stopwords_path = os.path.join(settings.BASE_DIR, "db_manager/datasets/stopwords.txt")


# WEBCRAWLER

def data_extractor():
    """Dataset Extraction"""

    # Load WebPage
    try:
        req = urllib.request.Request(
            'http://springboardcourses.ie/results?keywords=&perPage=5',
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            })
    except IncompleteRead:
        req = urllib.request.Request(
            'http://springboardcourses.ie/results?keywords=&perPage=5',
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            })

    f = urllib.request.urlopen(req)
    soup = bs.BeautifulSoup(f, 'lxml')

    courses = []

    for course_div in soup.find_all('div', class_="panel panel-primary"):

        try:
            # Course Title
            title_div = course_div.find('div', class_="panel-heading").h3.text
            title_div = title_div.strip()
            title_div = title_div.replace("  ", "")

        except Exception as e:
            title_div = None

        try:
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
            ects_credits = first_row.find('div', class_="col-md-3")
            ects_credits = str(ects_credits).split('</strong> ')[1]
            ects_credits = ects_credits.split('<')[0]

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
            skill_list = skill_list.lower()

            # Course Link
            link = course_div.find('a')
            link = link.get('href')


        except Exception as e:
            provider = None
            award = None
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
                        "ote_flag": ote_flag, "skill_list": skill_list, "link": link})

    return courses
