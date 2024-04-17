from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

from . import db

class Student(db.Model):
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    year_of_graduation = db.Column(db.Integer, nullable=False)
    major = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    profile = db.relationship('Profile', back_populates='student', uselist=False, lazy='joined')
    friends = db.relationship('Friend', backref='student', lazy=True)
    enrollments = db.relationship('Enrollment', back_populates='student')

class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), unique=True)
    biography = db.Column(db.Text)
    student = db.relationship('Student', back_populates='profile')

class Friend(db.Model):
    __tablename__ = 'friends'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
    friend_id = db.Column(db.Integer, db.ForeignKey('student.student_id'))
    status = db.Column(db.String(10), nullable=False, default='requested')

class Course(db.Model):
    __tablename__ = 'course'
    crn = db.Column(db.Integer, primary_key=True)
    course_title = db.Column(db.String(100), nullable=False)
    professor = db.Column(db.String(100), nullable=False)
    days_of_week = db.Column(db.String(50), nullable=False)
    class_time = db.Column(db.String(50), nullable=False)
    enrollments = db.relationship('Enrollment', back_populates='course')

class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    student_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), primary_key=True)
    crn = db.Column(db.Integer, db.ForeignKey('course.crn'), primary_key=True)
    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')
