from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from variables import db


class UserModel(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    phone_number = db.Column(db.String(10), nullable=False, default="N/A")
    address = db.Column(db.String(50), nullable=False, default="N/A")
    password = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False, default="N/A")
    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)


class DonationModel(db.Model):
    __tablename__ = 'donations'
    donation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    donee_id = db.Column(db.String(30), nullable=False)
    user_name = db.Column(db.String(30), ForeignKey('users.name'))
    name = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, default=func.now())
    description = db.Column(db.String(500), nullable=False)
    value = db.Column(db.Integer, nullable=False)


class PostModel(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    charity_name = db.Column(db.String(30), ForeignKey('users.name'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(30), nullable=False)
    phone_number = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    value = db.Column(db.Integer, nullable=False, default=0)
    time_created = db.Column(db.DateTime, default=func.now())
    contributions = db.Column(db.Integer, nullable=False, default=0)


class PostContributionModel(db.Model):
    __tablename__ = 'post_contributions'
    username = db.Column(db.String(30), ForeignKey('users.name'), primary_key=True)
    post_id = db.Column(db.Integer, ForeignKey('posts.id'), primary_key=True)
    value = db.Column(db.Integer, nullable=False, default=0)
