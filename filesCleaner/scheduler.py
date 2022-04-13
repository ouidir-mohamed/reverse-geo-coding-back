from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from . import filesCleaner

def start():
        print("hiiii start")
        scheduler = BackgroundScheduler()
        scheduler.add_job(task, 'interval', minutes=10)
        scheduler.start()
    

def task():
    filesCleaner.deleteOutdatedFiles()