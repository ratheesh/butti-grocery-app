# from __main__ import app
# from backend import app
# from flask import current_app as app
# celery = app.extensions["celery"]
from celery import shared_task
from celery.schedules import crontab
import os


@shared_task()
def sample_task():
    print("hello world")
    # os.system("sleep 3")
    return "hello world"

@shared_task()
def add_task():
    print("addition task")
    # os.system("sleep 3")
    return "addition task"