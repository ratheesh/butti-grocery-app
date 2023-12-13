import os
from datetime import datetime,timedelta
import base64

DB_FILE = "butti.sqlite3"

basedir = os.path.abspath(os.path.dirname(__file__))
db_file = "sqlite:///" + os.path.join(basedir, DB_FILE)
dbfile = os.path.join(basedir, DB_FILE)
UPLOAD_FOLDER = os.path.join(basedir, '../static/')

class Config():
    SECRET_KEY = "butti000"
    SQLALCHEMY_DATABASE_URI = db_file
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=10)
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
    CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
    CACHE_TYPE='RedisCache'
    CACHE_REDIS_URL='redis://localhost:6379/2'
    CACHE_DEFAULT_TIMEOUT=200