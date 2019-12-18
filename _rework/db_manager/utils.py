import csv
import os

from django.conf import settings

from core.models import Course


def database_upload(course_list):
    courses = Course.objects.all()
    courses.delete()

    for row in course_list:
        try:
            _, created = Course.objects.get_or_create(title=row['title'], provider=row['provider'], award=row['award'],
                                                      ects_credits=row['ects_credits'], mode=row['mode'],
                                                      deadline=row['deadline'],
                                                      start_date=row['start_date'], end_date=row['end_date'],
                                                      nfq=row['nfq'],
                                                      ote_flag=row[' ote_flag'], link=row['link'], skills=row['skill']
                                                      )
        except:
            pass