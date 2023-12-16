import os
from flask import request, jsonify,abort, make_response, send_file
from datetime import datetime, timedelta
from functools import wraps
from flask import Blueprint
import json
from sqlalchemy import desc, func, or_, and_
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)

from application.models import User,Product, Category, Order
from application.jwt import access
from application.db import db
from application.cache import cache

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
        return make_response('user not found', 404)
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
    try:
        products = Product.query.filter(Product.expiry_date >= datetime.now()).all()
    except:
        return make_response(jsonify("error getting products"), 500)

    return make_response(jsonify([product.to_dict() for product in products]), 200)
    
@routes.route("/admin", methods=["GET"])
@jwt_required()
@access(["admin"])
def admin():
    data = {}
    data["users"] = User.query.count()
    data["category"] = Category.query.count()
    data["products"] = Product.query.count()
    data["orders_total"] = Order.query.count()
    data["managers"] = User.query.filter_by(role='manager').count()
    data["users"] = User.query.filter_by(role='user').count()
    data["revenue_total"] = Order.query.filter().with_entities(func.sum(Order.total_amount)).scalar()
    
    # data["orders_today"] = Order.query.filter(func.date(Order.created_timestamp) == datetime.today().date()).count()
    
    # orders from past 7 days
    orders_data = []
    for i in range(7):
        date = datetime.now() - timedelta(days=i)
        count = Order.query.filter(func.date(Order.created_timestamp) == date.date()).count()
        orders_data.append({"date":date.date().strftime('%d/%b'), "count": count})
    data["orders"] = orders_data

    # category wise products
    category_data = []
    categories = Category.query.all()
    for category in categories:
        category_dict = category.to_dict()
        category_data.append({'name':category_dict['name'], 'count': len(category.products)})
        # category_data.append(([category.to_dict(), len(category.products)]))
    data["categories"] = category_data
    
    #Revenue from past 7 days
    revenue_data = []
    for i in range(7):
        date = datetime.now() - timedelta(days=i)
        revenue = Order.query.filter(func.date(Order.created_timestamp) == date.date()).with_entities(func.sum(Order.total_amount)).scalar()
        if revenue is None:
            revenue = 0
        revenue_data.append({"date":date.date().strftime('%d/%b'), "total":revenue})
    data["revenue"] = revenue_data

    return jsonify(data), 200


@routes.route("/manager", methods=["GET"])
@jwt_required()
@access(["manager"])
def manager():
    data = {}
    data["category"] = Category.query.count()
    data["products"] = Product.query.count()
    # data["revenue_today"] = 0
    data["revenue_today"] = Order.query.filter(func.date(Order.created_timestamp) == datetime.today().date()).with_entities(func.sum(Order.total_amount)).scalar()
    data["orders_today"] = Order.query.filter(func.date(Order.created_timestamp) == datetime.today().date()).count()
    
    # orders from past 7 days
    orders_data = []
    for i in range(7):
        date = datetime.now() - timedelta(days=i)
        count = Order.query.filter(func.date(Order.created_timestamp) == date.date()).count()
        orders_data.append({"date":date.date().strftime('%d/%b'), "count": count})
    data["orders"] = orders_data

    # category wise products
    category_data = []
    categories = Category.query.all()
    for category in categories:
        category_dict = category.to_dict()
        category_data.append({'name':category_dict['name'], 'count': len(category.products)})
        # category_data.append(([category.to_dict(), len(category.products)]))
    data["categories"] = category_data
    
    #Revenue from past 7 days
    revenue_data = []
    for i in range(7):
        date = datetime.now() - timedelta(days=i)
        revenue = Order.query.filter(func.date(Order.created_timestamp) == date.date()).with_entities(func.sum(Order.total_amount)).scalar()
        if revenue is None:
            revenue = 0
        revenue_data.append({"date":date.date().strftime('%d/%b'), "total":revenue})
    data["revenue"] = revenue_data

    return jsonify(data), 200

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

@routes.route("/search", methods=["GET"])
@jwt_required()
@access(["user"])
def search():
    '''search products'''
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    if current_user.role != "user":
        return make_response(jsonify("unauthorized"), 403)
    else:
        query = request.args.get('query')
        if query is None:
            return make_response(jsonify("empty search"), 400)

        categories = Category.query.filter(
            and_(Category.approved == True , Category.name.ilike("%" + query + "%"))
            ).all()

        category_products = []
        print(categories)
        for category in categories:
            category_products.extend([product for product in category.products if product.expiry_date >= datetime.now()])
            print(category_products)
            # category_products.extend(filter( lambda x: x.expiry_date >= datetime.now(), categories.products))

        products = Product.query.filter(
            and_(Product.expiry_date >= datetime.now() ,
            or_(Product.name.ilike("%" + query + "%") ,
            Product.description.ilike("%" + query + "%") ,
            Product.unit.ilike("%" + query + "%") ,
            Product.expiry_date.ilike("%" + query + "%") ,
            Product.price.ilike("%" + query + "%")))
            ).all()
        
        data = jsonify([category_product.to_dict() for category_product in category_products],
                       [product.to_dict() for product in products])
        return make_response(data, 200)
