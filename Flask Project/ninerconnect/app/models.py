from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, redirect, url_for, flash, render_template


from . import db

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    year_of_graduation = db.Column(db.Integer, nullable=False)
    major = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Course(db.Model):
    __tablename__ = 'course'
    id = db.Column(db.Integer, primary_key=True)
    course_prefix = db.Column(db.String(10), nullable=False)
    course_number = db.Column(db.Integer, nullable=False)
    course_professor = db.Column(db.String(100), nullable=False)
    student_email = db.Column(db.String(100), db.ForeignKey('student.email'))
    student = db.relationship('Student', back_populates='courses')

Student.courses = db.relationship('Course', back_populates='student', order_by=Course.id)


