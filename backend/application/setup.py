import os
import base64

from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_restful import Api
from flask_caching import Cache
from datetime import datetime,timedelta
from celery.schedules import crontab
from flask_jwt_extended import JWTManager

from .api import api, UserAPI, CategoryAPI, ProductAPI, OrderAPI
from .routes import routes
from .db import db
from .models import User, create_initial_data
from .celery_worker import celery_init_app
from .tasks import send_daily_reminder, send_monthly_reminder


DB_FILE = "butti.sqlite3"

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_file = "sqlite:///" + os.path.join(basedir, DB_FILE)
    app = Flask(__name__, template_folder="templates")
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    app.debug = True
    
    app.config["SECRET_KEY"] = "butti000"
    app.config['JWT_SECRET_KEY'] = base64.b64decode(app.config['SECRET_KEY'])
    app.config["SQLALCHEMY_DATABASE_URI"] = db_file
    app.config["UPLOAD_FOLDER"] = basedir
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=10)
    app.config["broker_url"] = "redis://localhost:6379/0"
    app.config["result_backend"] = "redis://localhost:6379/0"
    app.config["broker_connection_retry_on_startup"] = True
    app.app_context().push()
    
    CORS(app)
    hapi = Api(app)
    db.init_app(app)
    app.app_context().push()
    cache = Cache(app, config={'CACHE_TYPE': 'simple'})
    app.app_context().push()
    
    celery = celery_init_app(app)
    
    dbfile = os.path.join(basedir, DB_FILE)
    if not os.path.exists(dbfile):
        print("db file: ", dbfile)
        print("==== DB File does not exist, Creating one =====")
        db.create_all()
        print("==== Creating Admin and Common Categories =====")
        create_initial_data(db)
    
    jwt = JWTManager(app)
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id
    
    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()
    
    @jwt.invalid_token_loader
    def invalid_token_callback(msg):
        return make_response('invalid token', 401)
        
    @jwt.invalid_token_loader
    def invalid_token_callback(msg):
        return make_response('token expired', 401)
    
    app.register_blueprint(routes, url_prefix="/")
    app.register_blueprint(api, url_prefix="/api")
    
    hapi.add_resource(UserAPI, "/api/user", "/api/user/<username>")
    hapi.add_resource(CategoryAPI, "/api/category", "/api/category/<int:category_id>")
    hapi.add_resource(ProductAPI, "/api/product", "/api/product/<int:category_id>", "/api/product/<int:category_id>/<int:product_id>")
    # hapi.add_resource(BookmarkAPI, "/api/bookmark/<int:product_id>", "/api/bookmark/<int:product_id>/<int:bookmark_id>")
    hapi.add_resource(OrderAPI, "/api/order", "/api/order/<int:id>")
    
    return celery, app
    
    # @celery.on_after_finalize.connect
    # def setup_periodic_tasks(sender, **kwargs):
    #     sender.add_periodic_task( crontab(minute='*'), send_daily_reminder.s(), name='add daily reminder email')
    #     sender.add_periodic_task( crontab(minute='2'), send_monthly_reminder.s(), name='perform monthly task')

# End of File