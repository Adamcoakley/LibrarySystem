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
        
# test to add a book
class TestAddBook(TestBase):
    def test_add_book(self):
        response = self.client.post(
            url_for('admin_books'),
            data = dict(
                title = "The Great Gatzby",
                author = "F.Scott Fitagerald",
                num_of_copies = 10,
                description = "A 1925 novel set in the jazz age.",
            ),
            follow_redirects = True
        )

# test to delete a book
class TestDeleteBook(TestBase):
    def test_delete_book(self):
        response = self.client.delete(
            url_for('admin_books'),
            data = dict(
                title = "The Great Gatzby",
                author = "F.Scott Fitagerald",
                num_of_copies = 10,
                description = "A 1925 novel set in the jazz age.",
            ),
            follow_redirects = True
        )


