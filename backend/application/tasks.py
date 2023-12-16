# from celery import shared_task
from flask import render_template
from jinja2 import Template
from celery.schedules import crontab
from application.celery_worker import celery
from application.utils import send_email
from application.models import User, Product
import csv
import os
from datetime import datetime, date

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

@celery.task()
def send_csv_report(username):
    # return "send_csv_report"
    user = User.query.filter_by(username=username).first()
    if not user:
        return "user not found",404
    if user.role != "manager":
        return "user not authorized",403

    user = user.to_dict()
    products = Product.query.all()
    
    report_filename = f"{username}_product_report.csv"
    date = datetime.now().date()
    timestamp = datetime.now().strftime("%a %b %d %Y %I:%M:%S %p")
    if os.path.exists(report_filename):
        os.remove(report_filename)
    with open(report_filename, "w", newline='') as f:
        f = csv.writer(f, delimiter=',')
        f.writerow(["", "","", "Butti Groceries", "", "", ""])
        f.writerow(["", "Date",date, "", "", "", ""])
        f.writerow(["Name", "Description","Category", "Price", "Total Stock", "Stock Available", "Stock Sold"])
        for product in products:
            product_dict = product.to_dict()
            f.writerow([product.name, product.description,product_dict['category_name'], product.price, product.stock, product.stock_available, product.stock_sold])
        f.writerow(["", "Generated at",timestamp, "", "Butti Admin", "", ""])

    template_str = """
        <p>
            Dear {{ user }},
        </p>
        <br />
        <p>
            Please find the attached exported CSV file for the products in our store as on date.
        <br />
            The data provided in the CSV file is the same as the data you see in the Products page of the manager dashboard.
        <br />
            In case of any issues, please contact admin(admin@butti.com)
        <br />
        <p>
            Best regards,
        <br />
            Butti Grocery Store
        </p>
        """
    template = Template(template_str)

    address = user["email"]
    subject = "[Butti] Product Report"
    message = template.render(user=user["name"])

    file = open(report_filename, "rb")

    send_email(address, subject, message, attachment=file, filename=report_filename, subtype="csv")
    os.remove(report_filename)
