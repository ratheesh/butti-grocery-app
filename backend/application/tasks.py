from celery import shared_task
from celery.schedules import crontab
import os

@shared_task()
def send_daily_reminder():
    template = """
    <p>
        Dear M/s. {{ user }},
    </p>
    <br />
    <p>
        We really miss you on our Grocery Store.
    </p>
    <p>
        Check out our latest grocery products. They are always fresh and available at a affordable price.
    </p>
    <p>
        Eat Healthy, Stay Healthy!
    </p>
    <br />
    <p>
        Best regards,
    </p>
    <p>
        Butti Grocery Store
        """
    users = get_all_users()
    template = Template(template_str)

    for user in users:
        user_dict = user.to_dict()
        if not user_dict["posted"] and user_dict["username"] != "[deleted]":
            address = user_dict["email"]
            subject = user_dict["username"] + ", a friendly reminder to contribute to Blog-Lite"
            rendered_template = template.render(user=user_dict["username"], your_name="Blog-Lite")

            send_email(address, subject, rendered_template)
            
            user.posted = 0
            db.session.commit()

        folder_path = "static/img/Analytics/" + user_dict["username"]

        if os.path.exists(folder_path):
            try:
                shutil.rmtree(folder_path)
            except OSError as e:
                pass


    return 200


@shared_task()
def send_monthly_reminder():
    print("send monthly reminder")
    return "send monthly reminder"
