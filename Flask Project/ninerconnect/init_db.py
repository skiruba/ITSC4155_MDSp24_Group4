# Assuming your Flask application structure has an 'app' directory with an __init__.py that contains the create_app function.
from app import create_app, db  # Importing create_app and db from the app package

app = create_app()  # Create an instance of the Flask application

with app.app_context():
    db.drop_all()  # Warning: This will drop all existing tables, use with caution!
    db.create_all()  # Creates tables based on your SQLAlchemy models from models.py

