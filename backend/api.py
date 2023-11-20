from datetime import datetime
import os
import base64
import secrets

from flask import Blueprint, make_response, abort, Response
from flask_restful import NotFound, Resource, fields, marshal_with, reqparse, request
from werkzeug.exceptions import HTTPException
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required

from .db import db
from .models import User, Category, Product, Item, Bookmark, Order

api = Blueprint("api", __name__)


class BadRequest(HTTPException):
    def __init__(self, message):
        self.response = make_response(message, 400)
class AlreadyExists(HTTPException):
    def __init__(self, message):
        self.response = make_response(message, 409)

class Unauthorized(HTTPException):
    def __init__(self, message):
        self.response = make_response(message, 401)


class NotFound(HTTPException):
    def __init__(self, message):
        self.response = make_response(message, 404)


class InternalError(HTTPException):
    def __init__(self, message):
        self.response = make_response(message, 500)


user_request_parse = reqparse.RequestParser(bundle_errors=True)
user_request_parse.add_argument("name", type=str, required=True)
user_request_parse.add_argument("username", type=str, required=True)
user_request_parse.add_argument("email", type=str, required=True)
user_request_parse.add_argument("role", type=str, required=True)
user_request_parse.add_argument("password", type=str, required=True)
user_request_parse.add_argument("image_name", type=str, required=True)
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
    "image_name": fields.String,
    # "image": fields.String,
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
        image_name = args.get("image_name", None)

        # if args is None or name is None or username is None or password is None:
        if name is None or name == '':
            raise BadRequest("name not provided")
        if username is None or username == '':
            raise BadRequest("username not provided")
        if email is None or email == '':
            raise BadRequest("email not provided")
        if role is None or role == '':
            raise BadRequest("role not provided")
        else:
            if role == 'admin':
                raise BadRequest("Admin role can not be created")
        if password is None or password == '':
            raise BadRequest("password not provided")
        # if len(password) < 4:
        #     raise BadRequest("password length is less than 4 chars")
        if image_name is None or image_name == "":
            image_name = 'default.png'

        # check if the user already exists based on username
        user = User.query.filter_by(username=username).first()
        if user is not None:
            print("=== user already exists === ")
            # raise BadRequest("user already exists")
            abort(Response("user already exists", 400))

        user = User(
            name=name,
            username=username,
            email=email,
            password=generate_password_hash(password),
            role=role,
            approved=False,
            image_name=image_name,
            created_timestamp=datetime.now(),
            updated_timestamp=datetime.now(),
        )
        if user is None:
            raise InternalError(message="Error in creating User")

        db.session.add(user)
        db.session.flush()

        image = args.get("image", None)
        if image is not None and image_name is None:
            raise BadRequest("image_name name not provided")
        elif image is not None: 
            try:
                image_name = image_name.split('.')[0] + '_' + str(user.id) + '.png'
                user.image_name = image_name

                file_data = base64.b64decode(image)
                basedir = os.path.abspath(os.path.dirname(__file__))
                filename= basedir + '/images/products/' + image_name
                print('Image filename to be saved: ', filename)
                with open(filename, 'wb') as f:
                    f.write(file_data)
            except:
                raise InternalError(message="Error in saving image")

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
product_request_parse.add_argument("image_name", type=str)
product_request_parse.add_argument("image", type=str)
# product_request_parse.add_argument("category_id", type=int)

product_response_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "unit": fields.String,
    "price": fields.Integer,
    "stock": fields.Integer,
    "expiry_date": fields.DateTime,
    "image_name": fields.String,
    "image": fields.String,
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
                image_file= basedir + '/images/products/' + product.image_name
                print('Image filename to be read: ', image_file)
                if os.path.isfile(image_file):
                    with open(image_file, 'rb') as f:
                        product.image = base64.b64encode(f.read()).decode('utf-8')
            return products, 200
        else:
            category=Category.query.filter_by(id=category_id).first()
            if category is None:
                raise NotFound("Category not found")

        if product_id is None:
            products = Product.query.filter_by(category_id=category_id).all()
            for product in products:
                basedir = os.path.abspath(os.path.dirname(__file__))
                image_file= basedir + '/images/products/' + product.image_name
                print('Image filename to be read: ', image_file)
                if os.path.isfile(image_file):
                    with open(image_file, 'rb') as f:
                        product.image = base64.b64encode(f.read()).decode('utf-8')
            return products, 200
        else:
            product = Product.query.filter_by(category_id=category.id, id=product_id).first()
            if product is None:
                raise NotFound("Product not found")
            else:
                basedir = os.path.abspath(os.path.dirname(__file__))
                image_file= basedir + '/images/products/' + product.image_name
                print('Image filename to be read: ', image_file)
                if os.path.isfile(image_file):
                    with open(image_file, 'rb') as f:
                        product.image = base64.b64encode(f.read()).decode('utf-8')
                return product, 200

    # @jwt_required()
    @marshal_with(product_response_fields)
    def post(self, category_id):
        if category_id is None:
            raise BadRequest("Category id is missing")
        else:
            category=Category.query.filter_by(id=category_id).first()
            if category is None:
                raise NotFound("Category not found")

        args = product_request_parse.parse_args(strict=True)
        print(args)
        name = args.get("name", None)
        description = args.get("description", None)
        unit = args.get("unit", None)
        price = args.get("price", None)
        stock = args.get("stock", None)
        expiry_date = args.get("expiry_date", None)
        image_name = args.get("image_name", None)
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
            raise BadRequest("expiry date not provided")

        if image_name is None:
            image_name = 'default.png'
        else:
            image_name = secrets.token_hex(4) + '.png'


        product = Product(
            name=name,
            description=description,
            unit=unit,
            price=price,
            stock=stock,
            expiry_date=expiry_date,
            image_name=image_name,
            category_id=category_id,
            created_timestamp=datetime.now(),
            updated_timestamp=datetime.now(),
        )
        if product is None:
            raise InternalError(message="error creating product")
        
        db.session.add(product)
        db.session.flush()

        print(image_name, image)
        if image_name is not None and image is not None: 
            try:
                if image_name == "":
                    raise BadRequest("image_name is empty")

                # image_name = image_name.split('.')[0] + '_' + str(product.id) + '.png'
                product.image_name = image_name

                file_data = base64.b64decode(image)
                basedir = os.path.abspath(os.path.dirname(__file__))
                filename= basedir + '/images/products/' + image_name
                print('Image filename to be saved: ', filename)
                with open(filename, 'wb') as f:
                    f.write(file_data)
            except:
                raise InternalError(message="Error in saving image")
        else:
            image_name = 'default.png'
            product.image_name = image_name


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
                image_name = args.get("image_name", None)
                
                print('image_name: ', image_name, 'product imagename:', product.image_name)
                if image_name is None:
                    image_name = product.image_name
                
                if image is not None: 
                    try:
                        # image_name = image_name.split('.')[0] + '_' + str(user.id) + '.png'

                        if product.image_name == 'default.png':
                            image_name = secrets.token_hex(4) + '.png'
                        else:
                            image_name = product.image_name

                        file_data = base64.b64decode(image)
                        basedir = os.path.abspath(os.path.dirname(__file__))
                        filename= basedir + '/images/products/' + image_name
                        print('Image filename to be saved: ', filename)
                        with open(filename, 'wb') as f:
                            f.write(file_data)
                            os.sync()
                    except:
                        raise InternalError(message="Error in saving image")

                product.name = name
                product.description = description
                product.unit = unit
                product.price = price
                product.stock = stock
                product.expiry_date = expiry_date
                product.image_name = image_name
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
                image_name = product.image_name
                db.session.delete(product)
                db.session.commit()
                
                if image_name != 'default.png':
                    basedir = os.path.abspath(os.path.dirname(__file__))
                    filename= basedir + '/images/products/' + image_name
                    if os.path.isfile(filename):
                        try:
                            os.remove(filename)
                        except:
                            raise InternalError('deleting the image file')
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
