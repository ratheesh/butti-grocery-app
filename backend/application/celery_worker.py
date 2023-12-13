from flask import current_app as app
from celery import Celery, Task

celery = Celery('celery worker')

class FlaskTask(Task):
    def __call__(self, *args: object, **kwargs: object) -> object:
        with app.app_context():
            return self.run(*args, **kwargs)

