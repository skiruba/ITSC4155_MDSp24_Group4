from flask import Blueprint, flash, render_template, redirect, url_for, request
from .models import db, Student

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        # Your registration logic here
        existing_user = Student.query.filter_by(username=username).first()
        if existing_user is None:
            new_user = Student(fullname=fullname, email=email, username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            # login new user or redirect to login
            return redirect(url_for('.login'))
        else:
            flash('Username already exists')
    return render_template('signup.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Your user validation logic here
        user = Student.query.filter_by(username=username).first()
        if user and user.check_password(password):
            # login the user
            return redirect(url_for('.home'))
        else:
            # handle login failed
            flash('Invalid username or password')
    return render_template('login.html')

