from flask import Blueprint, flash, render_template, redirect, url_for, request, session, jsonify
from .models import Course, db, Student

main = Blueprint('main', __name__)

@main.route('/')
def init():
    return render_template('login.html')

@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        year_of_graduation = request.form['year_of_graduation']
        major = request.form['major']

        existing_user = Student.query.filter_by(username=username).first()
        if existing_user is None:
            new_user = Student(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                year_of_graduation=year_of_graduation,
                major=major,
            )
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('main.login'))
        else:
            flash('Username already exists', 'error')
    return render_template('signup.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Student.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['email'] = user.email  # Store user's email in session
            flash('Login successful!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@main.route('/logout')
def logout():
    session.pop('email', None)  # Clear the email from session on logout
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.login'))

@main.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if 'email' not in session:
        flash('You need to login first.', 'warning')
        return redirect(url_for('main.login'))

    student = Student.query.filter_by(email=session['email']).first()
    if not student:
        flash('Student not found. Please login again.', 'error')
        return redirect(url_for('main.login'))

    if request.method == 'POST':
        course_prefix = request.form.get('course_prefix')
        course_number = request.form.get('course_number')
        course_professor = request.form.get('course_professor')

        new_course = Course(
            course_prefix=course_prefix,
            course_number=int(course_number),
            course_professor=course_professor,
            student_email=student.email
        )
        db.session.add(new_course)
        db.session.commit()
        flash('Course added successfully!', 'success')
    
    courses = Course.query.filter_by(student_email=student.email).all()
    return render_template('add_course.html', courses=courses)

@main.route('/find_friends')
def find_friends():
    if 'email' not in session:
        flash('You must be logged in to access this page.', 'warning')
        return redirect(url_for('main.login'))

    # Retrieve data from the database
    courses = Course.query.all()

    # Render the template with the retrieved data
    return render_template('find_friends.html', courses=courses)

@main.route('/remove_course/<int:course_id>', methods=['GET', 'POST'])
def remove_course(course_id):
    if 'email' not in session:
        flash('You must be logged in to remove a course.', 'warning')
        return redirect(url_for('main.login'))

    course = Course.query.get(course_id)
    if course is None:
        flash('Course not found.', 'error')
        return redirect(url_for('main.add_course'))

    if request.method == 'POST':
        db.session.delete(course)
        db.session.commit()
        flash('Course removed successfully!', 'success')
        return redirect(url_for('main.add_course'))

    return render_template('remove_course.html', course=course)

@main.route('/profile')
def profile():
    if 'email' not in session:
        flash('You must be logged in to view your profile.', 'warning')
        return redirect(url_for('main.login'))

    user = Student.query.filter_by(email=session['email']).first()
    if not user:
        flash('User not found. Please log in again.', 'error')
        return redirect(url_for('main.login'))

    return render_template('profile.html', user=user)





