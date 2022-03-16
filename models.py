#here we use sqlalchemy for database
# sqlalchemy allows us to use classes and class like objects
from flask_sqlalchemy import SQLAlchemy
# from application import *

db = SQLAlchemy()

class User(db.Model):
    """User model"""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    #create_all will create the table as above specified columns
    #use it just once to create database

    # db.create_all()
