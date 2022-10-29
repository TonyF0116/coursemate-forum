from flask import Flask


def create_app():

    app = Flask(__name__, instance_relative_config=True,
                template_folder='./templates', static_folder='./templates/static')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'

    return app
