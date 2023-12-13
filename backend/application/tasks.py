# from celery import shared_task
from flask import render_template
from jinja2 import Template
from celery.schedules import crontab
from application.celery_worker import celery
from application.utils import send_email
from application.models import User
import os

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute='*'), 
        send_daily_reminder.s(), 
        name='send daily reminder email'
    )

    sender.add_periodic_task(
        crontab(minute='*/2'), 
        send_monthly_reminder.s(), 
        name='send monthly reminder email'
    )

@celery.task()
def send_daily_reminder():
    template = """
    <p>
        Dear M/s. {{ name }},
    </p>
    <br />
    <p>
        We really miss you on our Grocery Store.
    </p>
    <p>
        Check out our latest grocery products. They are always fresh and available at a affordable price.
    </p>
    <p>
        Excited to see you soon.
    </p>
    <br />
    <p>
        Best Regards,
    </p>
    <p>
        Butti Grocery Store
    </p>
        <small>Eat Healthy, Stay Healthy! </small>
        """
    users = User.query.all()
    template = Template(template)

    for user in users:
        user_dict = user.to_dict()
        if user_dict["role"] == "user":
            address = user_dict["email"]
            subject = "We miss you " + user_dict["name"].capitalize() + "!"
            rendered_template = template.render(name=user_dict["name"])
            send_email(address, subject, rendered_template)

    return 200


@celery.task()
def send_monthly_reminder():
    template = """
    <p>
        Dear M/s. {{ name }},
    </p>
    <br />
    <p> This is a monthly reminder</p>
    <br />
    <p>
        Best Regards,
    </p>
    <p>
        Butti Grocery Store
    </p>
        <small>Eat Healthy, Stay Healthy! </small>
        """
    users = User.query.all()
    template = Template(template)

    for user in users:
        user_dict = user.to_dict()
        if user_dict["role"] == "user":
            address = user_dict["email"]
            subject = "Butti Groceries Monthly Report"
            rendered_template = template.render(name=user_dict["name"])
            send_email(address, subject, rendered_template)

    return 200
