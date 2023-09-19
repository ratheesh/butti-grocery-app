import os
from flask import current_app as app
from flask import request, jsonify
from datetime import datetime, timedelta
from functools import wraps
from flask import Blueprint
# from sqlalchemy import desc, func, or_, and_
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required)
from .models import User, Token

from .db import db
from .models import User, Category, Product, Token

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
        return {"error": 404, "error_msg": "User not found"}
    if not check_password_hash(user.password, password):
        return {"error": 401, "error_msg": "Invalid Password"}
    access_token = create_access_token(identity=username)
    if access_token:
        token = Token(access_token=access_token, user_id=user.id)
        try:
            db.session.add(token)
            db.session.commit()
        except:
            return "Error Storing Token", 500
    return jsonify(access_token=access_token)

@routes.route("/logout", methods=['POST'])
def logout():
    return "logged out"