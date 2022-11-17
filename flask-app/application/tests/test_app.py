from application import app, db
from application.models import Book, User, Review, Request, Transaction, Record
from flask_testing import TestCase
from flask import url_for

# Create the base class
class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            SECRET_KEY='thisisasecretkey',
            debug=True,
            WTF_CSRF_ENABLE=False,
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()
        test_user = User(
            first_name = "James",
            last_name = "Smith",
            address = "123 Fake Street, Dublin",
            email = "James@gmail.com",
            password = "Password123",
            is_admin = 0,
        )
        test_record = Record(
            user_id = 1,
            num_books_hired = 0,
            num_books_returned = 0,
            current_num_books = 0,
        )
        test_book = Book(
            title = "Charlotte's Webb",
            author = 'E.B White',
            num_of_copies = 12,
            description = "The novel tells the story of a livestock pig named Wilbur and his friendship with a barn spider named Charlotte."
        )
        test_review = Review(
            user_id = 1,
            book_id = 1,
            title = "Charlotte's Webb",
            author = "E.B White",
            review = "I had to read this for school and I loved it!"
        )
        test_request = Request(
            user_id = 1,
            title = "Holes",
            author = "Louis Sachar",
            description = "The book centers on Stanley Yelnats who is sent to a boot camp is a desert in Texas after being falsely accused of theft."
        )
        test_transaction = Transaction(
            title = "Charlotte's Webb",
            author = "E.B White",
            issue_date = "17/11/2022",
            return_date = "17/02/2023",
            book_id = 1,
            user_id = 1,
        )
        # add test objects to db
        db.session.add(test_user)
        db.session.add(test_record)
        db.session.add(test_book)
        db.session.add(test_review)
        db.session.add(test_request)
        db.session.add(test_transaction)
        # commit to db 
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()
