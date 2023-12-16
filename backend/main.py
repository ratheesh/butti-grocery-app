import os
import base64

from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_restful import Api
from flask_caching import Cache
from datetime import datetime,timedelta
from celery.schedules import crontab
from flask_jwt_extended import JWTManager

from application.config import Config,dbfile
from application.routes import routes
from application.db import db
from application.cache import cache
from application.models import User, create_initial_data
from application import celery_worker

app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.debug = True
app.app_context().push()

CORS(app)
db.init_app(app)
cache.init_app(app)
celery=celery_worker.celery
celery.conf.update(
        broker_url=app.config["CELERY_BROKER_URL"],
        result_backend=app.config["CELERY_RESULT_BACKEND"],
        broker_connection_retry_on_startup=app.config["CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP"]
        )
celery.Task = celery_worker.FlaskTask
app.app_context().push()
app.extensions["celery"] = celery

app.app_context().push()

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


from application.api import api, UserAPI, CategoryAPI, ProductAPI, OrderAPI
hapi = Api(app)
hapi.add_resource(UserAPI, "/api/user", "/api/user/<username>")
hapi.add_resource(CategoryAPI, "/api/category", "/api/category/<int:category_id>")
hapi.add_resource(ProductAPI, "/api/product", "/api/product/<int:category_id>", "/api/product/<int:category_id>/<int:product_id>")
hapi.add_resource(OrderAPI, "/api/order", "/api/order/<int:id>")
app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(routes, url_prefix="/")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
