from application import db 

# User Table
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.DateTime(), nullable=False)
    is_admin = db.Column(db.Integer, nullable=False, default=0)
    record = db.relationship('Record', backref='record')
    rating = db.relationship('Rating', backref='rating')
    request = db.relationship('Request', backref='request')
    transaction = db.relationship('Transaction', backref='transaction')

# User Record Table
class Record(db.Model):
    record_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    num_books_hired = db.Column(db.Integer)
    num_books_returned = db.Column(db.Integer)
    current_num_books = db.Column(db.Integer)

# Books Table
class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    desc = db.Column(db.String(30), nullable=False)
    num_of_copies = db.Column(db.Integer, nullable=False)
    age_rating = db.Column(db.Integer, nullable=False)
    rating = db.relationship('Rating', backref='rating')
    transaction = db.relationship('Transaction', backref='transaction')

# Review Table
class Rating(db.Model):
    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    review = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

# Request Table
class Request(db.Model):
    request_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    title = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(30), nullable=False)

# Transaction Table
class Transaction(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    issue_date = db.Column(db.DateTime(), nullable=False)
    return_date = db.Column(db.DateTime(), nullable=False)
    returned = db.Column(db.Integer, nullable=False, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'))
    
# create database tables and relationships 
db.create_all()