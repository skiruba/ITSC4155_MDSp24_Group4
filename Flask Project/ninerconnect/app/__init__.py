from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(): # Create app
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=False, static_url_path='/static')
    app.config.from_object('config.Config')  

    db.init_app(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


