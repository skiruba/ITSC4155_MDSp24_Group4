import os

class Config:
    SECRET_KEY = '1234123412341234'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/mydatabase'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
