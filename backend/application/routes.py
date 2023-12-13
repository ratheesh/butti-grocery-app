import os
from flask import request, jsonify,abort, make_response, send_file
from datetime import datetime, timedelta
from functools import wraps
from flask import Blueprint
import json
# from sqlalchemy import desc, func, or_, and_
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
from .models import User,Product, Category
from .jwt import access
from .db import db

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
    
@routes.route("/home", methods=["GET"])
def home():
    '''home route'''
    products = Product.query.filter(Product.expiry_date > datetime.now()).all()
    return make_response(jsonify([product.to_dict() for product in products]), 200)

@routes.route("/approve", methods=["POST"])
@jwt_required()
@access(["admin"])
def approve():
    '''approve manager'''
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    if current_user.role != "admin":
        return make_response(jsonify("unauthorized"), 403)
    else:
        data = request.get_json()
        user_id = data.get("user_id")
        approved = data.get('approved')
        if approved == 'false':
            approved = False
        else:
            approved = True

        if user_id is None or approved is None:
            return make_response(jsonify("invalid request"), 400)

        user = User.query.get(user_id)
        print(user.name, user.role, approved)
        user.approved = approved
        try:
            db.session.add(user)
            cache.clear()
            db.session.commit()
        except:
            return jsonify("error approving user"), 500

        return make_response(jsonify(user=user.to_dict()),200)

@routes.route("/approvecategory", methods=["POST"])
@jwt_required()
@access(["admin"])
def approve_category(id):
    '''approve category'''
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    if current_user.role != "admin":
        return make_response(jsonify("unauthorized"), 403)
    else:
        data = request.get_json()
        user_id = data.get("user_id")
        approved = data.get('approved')
        if approved == 'false':
            approved = False
        else:
            approved = True

        if user_id is None or approved is None:
            return make_response(jsonify("invalid request"), 400)

        category = Category.query.get(id)
        category.approved = approved
        try:
            db.session.add(category)
            cache.clear()
            db.session.commit()
        except:
            return jsonify("error approving category"), 500

        return make_response(jsonify(category=category.to_dict()),200)
