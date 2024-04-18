import os

class Config:
    SECRET_KEY = '1234123412341234'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:isy120801@localhost:3306/college_scheduler'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
