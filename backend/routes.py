import os
from flask import current_app as app
from flask import request, jsonify,abort, make_response, send_file
from datetime import datetime, timedelta
from functools import wraps
from flask import Blueprint
import json
# from sqlalchemy import desc, func, or_, and_
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
from .models import User
from .jwt import access
from .tasks import sample_task, add_task

routes = Blueprint("controller", __name__)

@routes.route("/login", methods=["POST"])
def login():
    '''Login route'''
    print("In the login method")
    data = request.get_json()
    print(data)
    username, password = data.get("username"), data.get("password")
    user = User.query.filter_by(username=username).first()
    if not user:
        return make_response('user not found', 400)
    if not check_password_hash(user.password, password):
        return make_response('invalid password', 400)
    
    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)
    if not access_token or  not refresh_token:
        return make_response("error generating Token", 500)
    else:
        return jsonify(user=user.to_dict(), access_token=access_token)

@routes.route("/logout", methods=['POST'])
@jwt_required()
def logout():
    return "logged out",200

# @routes.route("/<path:path>", methods=["GET"])
# def send_image(path):
#     '''serve images'''
#     img_path=os.path.join(app.config["UPLOAD_FOLDER"], path)
#     print(img_path)
#     if os.path.isfile(img_path):
#         return send_file(img_path, mimetype='image/png')
#     else:
#         return jsonify("image not found"), 404
    

@routes.route("/test", methods=["GET"])
@jwt_required()
@access(["admin"])
def test():
    '''test route'''
    return jsonify(user=user.to_dict()),200
    
@routes.route('/celery', methods=['GET'])
def celery():
    '''celery route'''
    sample_task.delay()
    return jsonify("celery task executed"),200

@routes.route('/celery_add', methods=['GET'])
def celery_add():
    '''celery route'''
    add_task.delay()
    return jsonify("celery add task executed"),200