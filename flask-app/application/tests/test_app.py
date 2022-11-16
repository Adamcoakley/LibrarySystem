# imports
#import sys
#sys.path.append('../../application')

from application import app, db
from application.models import Book, User
from flask_testing import TestCase
from flask import url_for

# Create the base class
class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///',
            SECRET_KEY='thisisasecretkey',
            debug=True,
            WTF_CSRF_ENABLE=False,
        )
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
