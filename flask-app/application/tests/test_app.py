from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Register

# Create the base class
class TestBase(TestCase):
    def create_app(self):
        # Pass in testing configurations for the app
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table schema
        db.create_all()
        # create test user
        test_user = Register(
            first_name="Adam",
            last_name="Coakley",
            address="123 Fake Street",
            email="Adam@gmail.com",
            password="Password",
            confirm_password="Password"
        )
        # add test user to database
        db.session.add(test_user)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()

# Write a test class for all the routes to make sure they run
class TestViews(TestBase):
    # login and register
    def test_login(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_register(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)

    # admin routes
    def test_admin_books(self):
        response = self.client.get(url_for('admin_books'))
        self.assertEqual(response.status_code, 200)

    def test_admin_reviews(self):
        response = self.client.get(url_for('admin_reviews'))
        self.assertEqual(response.status_code, 200)

    def test_admin_requests(self):
        response = self.client.get(url_for('admin_requests'))
        self.assertEqual(response.status_code, 200)

    def test_admin_accounts(self):
        response = self.client.get(url_for('admin_accounts'))
        self.assertEqual(response.status_code, 200)

    # user routes
    def test_user_books(self):
        response = self.client.get(url_for('user_books'))
        self.assertEqual(response.status_code, 200)

    def test_user_reviews(self):
        response = self.client.get(url_for('user_reviews'))
        self.assertEqual(response.status_code, 200)

    def test_user_requests(self):
        response = self.client.get(url_for('user_requests'))
        self.assertEqual(response.status_code, 200)

    def test_user_account(self):
        response = self.client.get(url_for('user_account'))
        self.assertEqual(response.status_code, 200)


    

