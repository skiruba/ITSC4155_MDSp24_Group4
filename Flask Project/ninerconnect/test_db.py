from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__) # Run this python application to test DB connection
app.config['SQLALCHEMY_DATABASE_URI'] = ''
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

try:
    with app.app_context():
        result = db.session.execute(text('SELECT 1'))
        print("Database connection OK:", result.scalar())
except Exception as e:
    print("Failed to connect to the database:", e)
