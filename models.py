from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from variables import db


class UserModel(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    street = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)


class DoneeModel(db.Model):
    __tablename__ = 'donees'
    id = db.Column(db.String(20), primary_key=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    street = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(10), nullable=False)


class DonationModel(db.Model):
    __tablename__ = 'donations'
    user_name = db.Column(db.String(30), ForeignKey('users.name'), primary_key=True)
    donee_id = db.Column(db.String(20), ForeignKey('donees.id'), primary_key=True)
    date = db.Column(db.DateTime, default=func.now(), primary_key=True)
    type = db.Column(db.String(30), nullable=False)
    value = db.Column(db.Integer, nullable=False)


class PostModel(db.Model):
    __tablename__ = 'posts'
    charity_name = db.Column(db.String(30), nullable=False, primary_key=True)
    user_name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(30), nullable=False)
    phoneNumber = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    time_created = db.Column(db.DateTime, default=func.now(), primary_key=True)
