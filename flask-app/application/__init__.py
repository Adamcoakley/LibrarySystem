from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 

# app definition
app = Flask(__name__)

# configure db
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# extra imports 
from application import routes
from application import models
