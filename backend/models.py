from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref,relationship
from werkzeug.security import generate_password_hash
from .db import db

class User(db.Model):
    '''User Model'''
    __tablename__ = "user"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    approved = db.Column(db.Boolean, nullable=False, default=False)
    role = db.Column(db.String(32), nullable=False, default="user")
    image_name = db.Column(db.String(32), default="default.png")
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())

    # bookmarks = db.relationship("Bookmark", backref="user", cascade="all, delete-orphan")
    orders = db.relationship("Order", backref="user", cascade="all, delete-orphan")
    bookmarks = db.relationship("Bookmark", backref="user", cascade="all, delete-orphan")
    # token = db.relationship("Token",backref=backref("user", uselist=False), cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email,
            "approved": self.approved,
            "role": self.role,
            "image_name": self.image_name,
            "created_timestamp": self.created_timestamp,
            "updated_timestamp": self.updated_timestamp,
            # "orders": [order.to_dict() for order in self.orders],
            # "bookmarks": [bookmark.to_dict() for bookmark in self.bookmarks],
        }

    def __repr__(self) -> str:
        return self.username


class Category(db.Model):
    '''Category Model'''
    __tablename__ = "category"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())

    products = db.relationship("Product", backref="category", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            # "products": [product.to_dict() for product in self.products],
        }


class Product(db.Model):
    '''Product Model'''
    __tablename__ = "product"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(256), nullable=False)
    unit = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    image_name = db.Column(db.String(64), default="default.png")
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())

    items = db.relationship("Item", backref="product", cascade="all, delete-orphan")
    bookmarks = db.relationship("Bookmark", backref="product", cascade="all, delete-orphan")
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "unit": self.unit,
            "price": self.price,
            "stock": self.stock,
            "expiry_date": self.expiry_date,
            "image_name": self.image_name,
            "created_timestamp": self.created_timestamp,
            "updated_timestamp": self.updated_timestamp,
            "category_id": self.category_id,
        }


class Item(db.Model):
    '''Item Model'''
    __tablename__ = "item"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    updated_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())

    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "quantity": self.quantity,
            "created_timestamp": self.created_timestamp,
            "updated_timestamp": self.updated_timestamp,
            # "products": [product.to_dict() for product in self.products],
            "product_id": self.product_id,
            "order_id": self.order_id,
        }


class Bookmark(db.Model):
    '''Bookmark Model'''
    __tablename__ = "bookmark"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    
    bookmark_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def to_dict(self):
        '''to_dict'''
        return {
            "id": self.id,
            "products": [product.to_dict() for product in self.products],
            "user_id": self.user_id,
        }

class Order(db.Model):
    '''Order Model'''
    __tablename__ = "order"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    total_amount = db.Column(db.Float, nullable=False)
    items = db.relationship("Item", backref="order",  cascade="all,delete-orphan")
    created_timestamp = db.Column(
        db.DateTime, nullable=False, default=datetime.now())
    
    name = db.Column(db.String(32), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(64), nullable=False)
    payment_mode=db.Column(db.String(16), nullable=False)
    delivery_date = db.Column(db.DateTime, nullable=False, default=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def to_dict(self):
        '''to_dict'''
        return {
            "id": self.id,
            "total_amount": self.total_amount,
            "name":self.name,
            "address":self.address,
            "phone":self.phone,
            "email":self.email,
            "payment_mode":self.payment_mode,
            "delivery_date":self.delivery_date,
            "items": [item.to_dict for item in self.items],
            "user_id": self.user_id,
        }


def create_admin_user(db):
    '''create admin user'''
    admin = User(
        name="Admin",
        username="admin",
        email="admin@butti.com",
        password=generate_password_hash("admin"),
        role="admin",
        approved = True,
        image_name = "default.png",
        created_timestamp=datetime.now(),
        updated_timestamp=datetime.now(),
    )
    db.session.add(admin)
    db.session.commit()

# End of File 