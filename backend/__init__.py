import os

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_caching import Cache
from datetime import datetime,timedelta

from .api import api, UserAPI, CategoryAPI, ProductAPI, BookmarkAPI, OrderAPI
from .routes import routes
from .db import db
from .models import User, create_admin_user
from flask_jwt_extended import JWTManager


DB_FILE = "butti.sqlite3"
# app = None

def create_app():
    '''Create the Flask backend'''
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_file = "sqlite:///" + os.path.join(basedir, DB_FILE)
    app = Flask(__name__, template_folder="templates")
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')

    app.debug = True

    app.config["SECRET_KEY"] = "butti-booking-app"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_file
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=10)

    CORS(app)
    hapi = Api(app)
    db.init_app(app)
    app.app_context().push()
    cache = Cache(app, config={'CACHE_TYPE': 'simple'})

    dbfile = os.path.join(basedir, DB_FILE)
    if not os.path.exists(dbfile):
        print("db file: ", dbfile)
        print("==== DB FILE DOES NOT EXIST, CREATING ONE =====")
        db.create_all()
        print("==== CREATING ADMIN USER =====")
        create_admin_user(db)

    jwt = JWTManager(app)
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()

    app.register_blueprint(routes, url_prefix="/")
    app.register_blueprint(api, url_prefix="/api")

    hapi.add_resource(UserAPI, "/api/user", "/api/user/<username>")
    hapi.add_resource(CategoryAPI, "/api/category", "/api/category/<category_id>")
    hapi.add_resource(ProductAPI, "/api/product/<category_id>", "/api/product/<category_id>/<product_id>")
    hapi.add_resource(BookmarkAPI, "/api/bookmark/<product_id>", "/api/bookmark/<product_id>/<bookmark_id>")
    hapi.add_resource(OrderAPI, "/api/order", "/api/order/<order_id>")

    return app

# End of File
