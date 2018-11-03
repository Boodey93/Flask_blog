from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c5e6ed12174bdec5c4213e69eb22ae48'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"
db = SQLAlchemy(app)

from flaskblog import routes