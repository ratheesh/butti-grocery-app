# from celery import shared_task
import os
import csv
from datetime import datetime, timedelta
import smtplib

from flask import render_template
from jinja2 import Template
from flask import render_template
from sqlalchemy import desc, func, or_, and_
from celery.schedules import crontab
from application.celery_worker import celery
from application.utils import send_email
from application.models import User, Product,Order
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

@celery.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute='0', hour='18' ),
        send_daily_reminder.s(),
        name='send daily reminder email'
    )

    sender.add_periodic_task(
        crontab(minute='0', hour='1', day_of_month='1'),
        send_monthly_report.s(),
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
            orders_today = Order.query.filter(Order.user_id==user_dict["id"]).filter(func.date(Order.created_timestamp) == datetime.now().date()).count()
            if orders_today == 0:
                address = user_dict["email"]
                subject = "We miss you " + user_dict["name"].capitalize() + "!"
                rendered_template = template.render(name=user_dict["name"])
                send_email(address, subject, rendered_template)
            else:
                print(f"User {user_dict['name']} has already ordered today")

    return 200


@celery.task()
def send_monthly_report():
    users = User.query.filter_by(role="user").all()

    for user in users:
        user = user.to_dict()

        orders = Order.query.filter(Order.user_id==user["id"]).filter(func.date(Order.created_timestamp) > datetime.now().date() - timedelta(days=30)).all()
        # total_amount = orders.with_entities(func.sum(Order.total_amount)).scalar()
        orders = [order.to_dict() for order in orders]
        for order in orders:
            order['nitems'] = len(order['items'])
            order['created_timestamp'] = order['created_timestamp'].strftime("%d/%m/%Y %H:%M:%S")
            order['delivery_date'] = order['delivery_date'].strftime("%d/%m/%Y")
        total_amount= sum([order['total_amount'] for order in orders])
        # print('orders len"', len(orders))
        # print(total_amount)

        SMTP_SERVER_HOST = "localhost"
        SMTP_SERVER_PORT = 1025
        SENDER_ADDRESS = "admin@butti.com"
        SENDER_PASSWORD = ""
        msg = MIMEMultipart()
        msg["From"] = SENDER_ADDRESS
        msg["To"] = user["email"]
        msg["Subject"] = "[Butti] User Monthly Report"

        template = render_template("user_report.html", user=user["username"], orders=orders, total_amount=total_amount)
        msg.attach(MIMEText(template, "html"))

        smtp = smtplib.SMTP(host=SMTP_SERVER_HOST, port=SMTP_SERVER_PORT)
        smtp.login(SENDER_ADDRESS, SENDER_PASSWORD)
        smtp.send_message(msg)
        smtp.quit()

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

    # return report_filename

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
