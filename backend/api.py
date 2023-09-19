from datetime import datetime

from flask import Blueprint, make_response
from flask_restful import NotFound, Resource, fields, marshal_with, reqparse, request
from werkzeug.exceptions import HTTPException
from werkzeug.security import check_password_hash, generate_password_hash

from .db import db
from .models import User

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
user_request_parse.add_argument("password", type=str)
user_request_parse.add_argument("image", type=str)
# user_request_parse.add_argument("image", type=werkzeug.datastructures.FileStorage)

user_response_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "username": fields.String,
    "password": fields.String,
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
        args = user_request_parse.parse_args(strict=True)
        name = args.get("name", None)
        username = args.get("username", None)
        password = args.get("password", None)

        # if args is None or name is None or username is None or password is None:
        if name is None:
            raise BadRequest("Name not provided")
        if username is None:
            raise BadRequest("Username not provided")
        if password is None:
            raise BadRequest("Password not provided")
        if len(password) < 4:
            raise BadRequest("Password length is less than 4 chars")

        # check if the user already exists based on username
        user = User.query.filter_by(username=username).first()
        if user is not None:
            print("=== user already exists === ")
            raise BadRequest("user already exists")

        user = User(
            name=name,
            username=username,
            password=generate_password_hash(password),
            role="user",
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

class CategoryAPI(Resource):
    pass

class ProductAPI(Resource):
    pass

# End of File
