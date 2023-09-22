from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref
from werkzeug.security import generate_password_hash
from .db import db

class User(db.Model):
    '''User Model'''
    __tablename__ = "user"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    admin_approved = db.Column(db.Boolean, nullable=False, default=False)
    role = db.Column(db.String(32), nullable=False, default="user")
    image = db.Column(db.String(32), default="default.jpg")
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())

    # bookmarks = db.relationship("Bookmark", backref="user", cascade="all, delete-orphan")
    bookmarks = db.relationship("Bookmark", backref="user", cascade="all, delete-orphan")
    token = db.relationship("Token",backref=backref("user", uselist=False), cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return self.username


class Token(db.Model):
    '''Token Model'''
    __tablename__ = "token"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    access_token = db.Column(db.String(256), nullable=False)
    refresh_token = db.Column(db.String(256), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class Category(db.Model):
    '''Category Model'''
    __tablename__ = "category"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(32), nullable=False)

    products = db.relationship("Product", backref="category", cascade="all, delete-orphan")


class Product(db.Model):
    '''Product Model'''
    __tablename__ = "product"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    unit = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)
    image = db.Column(db.String(32), default="default.jpg")
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())

    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    bookmark_id = db.Column(db.Integer, db.ForeignKey("bookmark.id"), nullable=False)


class Item(db.Model):
    '''Item Model'''
    __tablename__ = "item"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    count = db.Column(db.Integer, nullable=False)
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())

    products = db.relationship("Product",backref="product", cascade="all, delete-orphan")

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)


class Bookmark(db.Model):
    '''Bookmark Model'''
    __tablename__ = "bookmark"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    products = db.relationship("Product", backref="bookmark", cascade="all, delete-orphan")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

class Order(db.Model):
    '''Order Model'''
    __tablename__ = "order"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    items = db.relationship("Item", backref="order",  cascade="all,delete-orphan")

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


def create_admin_user(db):
    '''create admin user'''
    admin = User(
        name="Admin",
        username="admin",
        password=generate_password_hash("admin"),
        role="admin",
        admin_approved = True,
        image = "admin.png",
        created_timestamp=datetime.now(),
        updated_timestamp=datetime.now(),
    )
    db.session.add(admin)
    db.session.commit()

# End of File 