from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# app definition
app = Flask(__name__)

# configure db
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Hanover51@localhost:3306/library'
app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# extra imports 
from application import routes
from application import models
