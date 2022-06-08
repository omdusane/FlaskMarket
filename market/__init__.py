from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import path

DB_NAME = "market.db"
#to create database file if it does not exists
def create_database(app):
    if not path.exists('market/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SECRET_KEY'] = 'Sasuke'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
create_database(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

#To avoid Circular import
from .routes import routes
app.register_blueprint(routes, url_prefix="/")


