from flask import Flask
from .routes import index
from .db_config import connection


def create_app():

    app = Flask(__name__, instance_relative_config=True,
                template_folder='./templates', static_folder='./templates/static')

    # app.config['SQLALCHEMY_DATABASE_URI'] = connection
    # For local db testing
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'

    app.register_blueprint(index.bp)
    return app
