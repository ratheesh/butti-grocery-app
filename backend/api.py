from datetime import datetime
import os
import base64

from flask import Blueprint, make_response
from flask_restful import NotFound, Resource, fields, marshal_with, reqparse, request
from werkzeug.exceptions import HTTPException
from werkzeug.security import check_password_hash, generate_password_hash

from .db import db
from .models import User, Category, Product, Item, Bookmark, Order

api = Blueprint("api", __name__)


class BadRequest(HTTPException):
    def __init__(self, message):
        super().__init__(message, response=None)
        self.code = 400
        self.description = message


class Unauthorized(HTTPException):
    def __init__(self, message):
        super().__init__(message, response=None)
        self.code = 401
        self.description = message


class NotFound(HTTPException):
    def __init__(self, message):
        super().__init__(message, response=None)
        self.code = 404
        self.description = message


class InternalError(HTTPException):
    def __init__(self, message):
        super().__init__(message, response=None)
        self.code = 500
        self.description = message


user_request_parse = reqparse.RequestParser(bundle_errors=True)
user_request_parse.add_argument("name", type=str)
user_request_parse.add_argument("username", type=str)
user_request_parse.add_argument("email", type=str)
user_request_parse.add_argument("role", type=str)
user_request_parse.add_argument("password", type=str)
user_request_parse.add_argument("image", type=str)
# user_request_parse.add_argument("image", type=werkzeug.datastructures.FileStorage)

user_response_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "username": fields.String,
    "email": fields.String,
    "password": fields.String,
    "approved": fields.String,
    "role": fields.String,
    "image": fields.String,
    "created_timestamp": fields.DateTime,
    "updated_timestamp": fields.DateTime,
}

class UserAPI(Resource):
    """
    User Object for managing users
    """

    @marshal_with(user_response_fields)
    def get(self, username=None):
        if username:
            user = User.query.filter_by(username=username).first()
            if user:
                return user, 200
            else:
                raise NotFound("User not found")
        else:
            users = User.query.all()
            return users, 200

    @marshal_with(user_response_fields)
    def post(self):
        '''Create a new user'''
        args = user_request_parse.parse_args(strict=True)
        print(args)
        name = args.get("name", None)
        username = args.get("username", None)
        email = args.get("email", None)
        role = args.get("role", None)
        password = args.get("password", None)

        # if args is None or name is None or username is None or password is None:
        if name is None:
            raise BadRequest("name not provided")
        if username is None:
            raise BadRequest("username not provided")
        if email is None:
            raise BadRequest("email not provided")
        if role is None:
            raise BadRequest("role not provided")
        else:
            if role == 'admin':
                raise BadRequest("Admin role can not be created")
        if password is None:
            raise BadRequest("password not provided")
        # if len(password) < 4:
        #     raise BadRequest("password length is less than 4 chars")

        # check if the user already exists based on username
        user = User.query.filter_by(username=username).first()
        if user is not None:
            print("=== user already exists === ")
            raise BadRequest("user already exists")

        user = User(
            name=name,
            username=username,
            email=email,
            password=generate_password_hash(password),
            role=role,
            approved=False,
            image="default.jpg",
            created_timestamp=datetime.now(),
            updated_timestamp=datetime.now(),
        )
        if user is None:
            raise InternalError(message="Error in creating User")

        try:
            db.session.add(user)
            db.session.commit()
        except:
            raise InternalError(message="Error in creating User")

        return user, 201

    @marshal_with(user_response_fields)
    def put(self, username=None):
        if username is None:
            raise BadRequest("username not given")
        else:
            args = user_request_parse.parse_args(strict=True)

            name = args.get("name", None)
            password = generate_password_hash(args.get("password", None))

            user = User.query.filter_by(username=username).first()
            if user is not None:
                if user.username == "admin":
                    raise Unauthorized(message="Admin profile can not modified")

                user.name = name
                user.password = password
                user.updated_timestamp = datetime.now()
            else:
                raise NotFound(message="User not found")

            try:
                db.session.add(user)
                db.session.commit()
            except:
                raise InternalError(message="Error in updating User")

            return user, 200

    def delete(self, username=None):
        if username is None:
            raise BadRequest("User name is missing")
        else:
            user = User.query.filter_by(username=username).first()
            if user is None:
                raise NotFound(message="User not found")
            try:
                db.session.delete(user)
                db.session.commit()
            except:
                raise InternalError(message="Error deleting User")

        return "User deleted successfully", 200


category_request_parse = reqparse.RequestParser(bundle_errors=True)
category_request_parse.add_argument("name", type=str, required=True)

category_response_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "created_timestamp": fields.DateTime,
    "updated_timestamp": fields.DateTime,
}
class CategoryAPI(Resource):
    '''Category Object for managing categories'''
    @marshal_with(category_response_fields)
    def get(self, category_id=None):
        if category_id is None:
            categories = Category.query.all()
            return categories, 200
        else:
            category = Category.query.filter_by(id=category_id).one_or_none()
            if category is None:
                raise NotFound("category not found")
            else:
                return category, 200


    @marshal_with(category_response_fields)
    def post(self):
        args = category_request_parse.parse_args(strict=True)
        
        name = args.get("name", None)
        if name is None:
            raise BadRequest("name not provided")
        name = name.capitalize()

        category = Category.query.filter_by(name=name).first()
        if category is not None:
            print("=== category already exists === ")
            raise BadRequest("category already exists")

        category = Category(
            name=name,
            created_timestamp=datetime.now(),
            updated_timestamp=datetime.now(),
        )
        if category is None:
            raise InternalError(message="error creating category")

        try:
            db.session.add(category)
            db.session.commit()
        except:
            raise InternalError(message="error creating category")

        return category, 201
    
    @marshal_with(category_response_fields)
    def put(self, category_id):
        if category_id is None:
            raise NotFound("category id is missing")

        category = Category.query.filter_by(id=category_id).first()
        if category is None:
            return NotFound("category not found")
        else:
            args = category_request_parse.parse_args(strict=True)

            name = args.get("name", None)
            if name == "" or name is None:
                raise BadRequest("name is empty")
            else:
                name = name.capitalize()

            category.name = name
            category.updated_timestamp = datetime.now()

            try:
                db.session.add(category)
                db.session.commit()
            except:
                raise InternalError(message="error in updating category")

            return category, 200
    
    def delete(self, category_id):
        if id is None:
            raise BadRequest("category id is missing")

        category = Category.query.filter_by(id=category_id).first()
        if category is None:
            raise NotFound(message="Category not found")
        else:
            try:
                db.session.delete(category)
                db.session.commit()
            except:
                raise InternalError(message="error deleting category")
            
def valid_date(s):
    return datetime.strptime(s, "%Y-%m-%d %H:%M")

product_request_parse = reqparse.RequestParser(bundle_errors=True)
product_request_parse.add_argument("name", type=str, required=True)
product_request_parse.add_argument("description", type=str, required=True)
product_request_parse.add_argument("unit", type=str, required=True, default="piece")
product_request_parse.add_argument("price", type=int, required=True)
product_request_parse.add_argument("stock", type=int, required=True)
product_request_parse.add_argument("expiry_date", type=valid_date, required=True)
product_request_parse.add_argument("image", type=str, default="default.jpg")
product_request_parse.add_argument("image_file", type=str)
# product_request_parse.add_argument("category_id", type=int)

product_response_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "unit": fields.String,
    "price": fields.Integer,
    "stock": fields.Integer,
    "expiry_date": fields.DateTime,
    "image": fields.String,
    "image_file": fields.String,
    "created_timestamp": fields.DateTime,
    "updated_timestamp": fields.DateTime,
    "category_id": fields.Integer,
}
class ProductAPI(Resource):
    '''Product Object for managing products'''
    @marshal_with(product_response_fields)
    def get(self, category_id=None, product_id=None):
        if category_id is None:
            products = Product.query.all()
            # print(products)
            for product in products:
                basedir = os.path.abspath(os.path.dirname(__file__))
                image_file= basedir + '/images/products/' + product.image
                print('Image filename to be read: ', image_file)
                if os.path.isfile(image_file):
                    with open(image_file, 'rb') as f:
                        product.image_file = base64.b64encode(f.read())
            return products, 200
        else:
            category=Category.query.filter_by(id=category_id).first()
            if category is None:
                raise NotFound("Category not found")

        if product_id is None:
            products = Product.query.filter_by(category_id=category_id).all()
            return products, 200
        else:
            product = Product.query.filter_by(category_id=category.id, id=product_id).first()
            if product is None:
                raise NotFound("Product not found")
            else:
                return product, 200

    @marshal_with(product_response_fields)
    def post(self, category_id):
        if category_id is None:
            raise BadRequest("Category id is missing")
        else:
            category=Category.query.filter_by(id=category_id).first()
            if category is None:
                raise NotFound("Category not found")

        args = product_request_parse.parse_args(strict=True)
        # print(args)
        name = args.get("name", None)
        description = args.get("description", None)
        unit = args.get("unit", None)
        price = args.get("price", None)
        stock = args.get("stock", None)
        expiry_date = args.get("expiry_date", None)
        image = args.get("image", None)

        if name is None:
            raise BadRequest("name not provided")
        if description is None:
            raise BadRequest("description not provided")
        if unit is None:
            raise BadRequest("unit not provided")
        if price is None:
            raise BadRequest("price not provided")
        if stock is None:
            raise BadRequest("stock not provided")
        if expiry_date is None:
            raise BadRequest("expiry_date not provided")
        if image is None or image == "":
            image = 'default.jpg'

        product = Product(
            name=name,
            description=description,
            unit=unit,
            price=price,
            stock=stock,
            # expiry_date=expiry_date, # FIXME
            expiry_date=datetime.now(),
            image=image,
            category_id=category_id,
            created_timestamp=datetime.now(),
            updated_timestamp=datetime.now(),
        )
        if product is None:
            raise InternalError(message="error creating product")
        
        db.session.add(product)
        db.session.flush()

        file = args.get("image_file", None)
        if file is not None and image is None:
            raise BadRequest("image_file name not provided")
        else: 
            try:
                image = image.split('.')[0] + '_' + str(product.id) + '.jpg'
                product.image = image

                file_data = base64.b64decode(file)
                basedir = os.path.abspath(os.path.dirname(__file__))
                filename= basedir + '/images/products/' + image
                print('Image filename to be saved: ', filename)
                with open(filename, 'wb') as f:
                    f.write(file_data)
            except:
                raise InternalError(message="Error in saving image")

        try:
            db.session.add(product)
            db.session.commit()
        except:
            raise InternalError(message="error creating product")

        return product, 201
        
    @marshal_with(product_response_fields)
    def put(self, category_id, product_id):
        if category_id is None:
            raise BadRequest("category id is missing")
        else:
            category=Category.query.filter_by(id=category_id).first()
            if category is None:
                raise NotFound("category not found")

        if product_id is None:
            raise BadRequest("product id is missing")
        else:
            args=product_request_parse.parse_args(strict=True)
            print(args)
            product=Product.query.filter_by(category_id=category_id, id=product_id).first()
            if product is None:
                raise NotFound("product not found")
            else:
                name = args.get("name", None)
                description = args.get("description", None)
                unit = args.get("unit", None)
                price = args.get("price", None)
                stock = args.get("stock", None)
                expiry_date = args.get("expiry_date", None)
                image = args.get("image", None)

                product.name = name
                product.description = description
                product.unit = unit
                product.price = price
                product.stock = stock
                product.expiry_date = expiry_date
                product.image = image
                product.category_id = category_id
                product.updated_timestamp=datetime.now()

                try:
                    db.session.add(product)
                    db.session.commit()
                except:
                    raise InternalError(message="Error in updating product")

                return product, 200
    
    def delete(self, category_id, product_id):
        if category_id is None:
            raise BadRequest("category id is missing")
        if product_id is None:
            raise BadRequest("product id is missing")
        else:
            product=Product.query.filter_by(category_id=category_id, id=product_id).first()
            if product is None:
                raise NotFound("product not found")
            try:
                db.session.delete(product)
                db.session.commit()
            except:
                raise InternalError(message="error deleting product")

        return "product deleted successfully", 200

bookmark_request_parse = reqparse.RequestParser(bundle_errors=True)
bookmark_request_parse.add_argument("name", type=str)

bookmark_response_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "created_timestamp": fields.DateTime,
    "updated_timestamp": fields.DateTime,
    "user_id": fields.Integer,
}
class BookmarkAPI(Resource):
    '''Bookmarks Object for managing bookmarks'''
    def get(self, user_id, id=None):
        if user_id is None:
            raise BadRequest("User id is missing")
        else:
            user=User.query.filter_by(id=user_id).first()
            if user is None:
                raise NotFound("User not found")
        
        if id is None:
            bookmarks = Bookmark.query.filter_by(user_id=user.id).all()
            return bookmarks, 200
        else:
            bookmark = Bookmark.query.filter_by(user_id=user.id, id=id).first()
            if bookmark is None:
                raise NotFound("Bookmark not found")
            else:
                return bookmark, 200

    def post(self, user_id):
        if user_id is None:
            raise BadRequest("User id is missing")
        else:
            user=User.query.filter_by(id=user_id).first()
            if user is None:
                raise NotFound("User not found")
        
        args=user_request_parse.parse_args(strict=True)
        name = args.get("name", None)

        if name is None:
            raise BadRequest("name not provided")
        
        try:
            bookmark = Bookmark(
                name=name,
                user_id=user.id,
            )
            db.session.add(bookmark)
            db.session.commit()
        except:
            raise InternalError(message="error creating bookmark")
        
        return bookmark, 201

    
    def put(self, id):
        if id is None:
            raise BadRequest("Bookmark id is missing")
        
        bookmark=Bookmark.query.filter_by(id=id).first()
        if bookmark is None:
            raise NotFound("Bookmark not found")
        else:
            user_id=bookmark.user_id
            args=user_request_parse.parse_args(strict=True)
            name=args.get("name", None)

            bookmark.name=name
            bookmark.user_id=user_id
            bookmark.updated_timestamp=datetime.now()

            try:
                db.session.add(bookmark)
                db.session.commit()
            except:
                raise InternalError(message="Error in updating bookmark")
            
            return bookmark, 200

    def delete(self, id):
        if id is None:
            raise BadRequest("Bookmark id is missing")
        else:
            try:
                bookmark=Bookmark.query.filter_by(id=id).first()
                db.session.delete(bookmark)
                db.session.commit()
            except:
                raise InternalError(message="Error deleting bookmark")

        return "Bookmark deleted successfully", 200

order_request_parse = reqparse.RequestParser(bundle_errors=True)
order_request_parse.add_argument("name", type=str, required=True)
order_request_parse.add_argument("total_amount", type=float, required=True)
order_request_parse.add_argument("items", type=list, required=True)
order_request_parse.add_argument("user_id", type=int, required=True)

order_response_fields = {
    "id": fields.Integer,
    "total_amount": fields.Float,
    "items": fields.List,
    "created_timestamp": fields.DateTime,
    "user_id": fields.Integer,
}
class OrderAPI(Resource):
    '''Order Object for managing orders'''
    @marshal_with(order_response_fields)
    def get(self, user_id, id=None):
        if user_id is None:
            raise NotFound("User id is missing")
        if id is None:
            orders = Order.query.filter_by(user_id=user_id).all()
            return orders, 200
        else:
            order = Order.query.filter_by(user_id=user_id, id=id).first()
            if order is None:
                raise NotFound("Order not found")
            else:
                return order, 200 
    
    @marshal_with(order_response_fields)
    def post(self, user_id, items):
        if user_id is None:
            raise BadRequest("User id is missing")
        if items is None:
            raise BadRequest("Items are missing")
        else:
            user=User.query.filter_by(id=user_id).first()
            if user is None:
                raise NotFound("User not found")
            
            order = Order(
                items=items,
                total_amount=total_amount,
                user_id=user.id,
                created_timestamp=datetime.now(),
            )
            
            db.session.add(order)
            db.session.flush()

            items_list = []
            for item in items:
                new_item = Item(
                    product_id=item.product_id,
                    quantity=item.quantity,
                    order_id=order.id,
                    created_timestamp=datetime.now(),
                    updated_timestamp=datetime.now(),
                )
                items_list.append(new_item)
            try:
                db.session.add_all(items_list)
                db.session.add(order)
                db.session.commit()
            except:
                raise InternalError(message="error creating order")
    
    @marshal_with(order_response_fields)
    def put(self,id, user_id, items):
        if user_id is None:
            raise BadRequest("User id is missing")
        if id is None:
            raise BadRequest("Order id is missing")
        if items is None:
            raise BadRequest("Items are missing")

        order=Order.query.filter_by(id=id).first()
        if order is None:
            raise NotFound("Order not found")
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            raise NotFound("User not found")
        if items.len() == 0:
            raise BadRequest("Items list is empty")
        
        order.total_amount = total_amount
        order.items = items
        order.updated_timestamp = datetime.now()

        try:
            db.session.add(order)
            db.session.add_all(items)
            db.session.commit()
        except:
            raise InternalError(message="Error in updating order")
        
        return order, 200
    
    def delete(self, id):
        if id is None:
            raise BadRequest("Order id is missing")
        
        order=Order.query.filter_by(id=id).first()
        try:
            db.session.delete(order)
            db.session.commit()
        except:
            raise InternalError(message="Error deleting order")
        return "Order deleted successfully", 200
        

# End of File
