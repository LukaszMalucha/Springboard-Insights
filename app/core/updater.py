from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from api import utils


def start():
    scheduler = BackgroundScheduler()

    scheduler.add_job(utils.data_extractor, trigger="interval", seconds=600)


    scheduler.start()
