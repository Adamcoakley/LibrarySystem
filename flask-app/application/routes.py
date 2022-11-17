from application import app, db
from flask import render_template, request, redirect, url_for, flash, session
from application.forms import Register, Login, Requests
from application.models import User, Book, Review, Request, Record, Transaction
import bcrypt
from datetime import date
from dateutil.relativedelta import relativedelta

# function to add a book to the database
def add_book():
    # create a new user object
    new_book = Book(
        title = request.form['title'],
        author = request.form['author'],
        description = request.form['description'],
        num_of_copies = request.form['copies'],
    )
    # add and commit book to database
    db.session.add(new_book)
    db.session.commit()
    # flash message 
    flash("Book added successfully.")

# authentication routes (login + register)
# login page 
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        # check if a user exists
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            # passwords need to be encodede to be compared
            form_pass = form.password.data.encode('UTF-8')
            user_pass = user.password.encode('UTF-8')
            # user exists, check if their password is correct
            if bcrypt.checkpw(form_pass, user_pass):
                # password is correct, check if the user is an admin (1) or standar user (0)
                if user.is_admin == 0:
                    # create a session for the user 
                    session["user_id"] = user.user_id
                    return redirect(url_for("user_books"))
                else:
                    # create a session for the admin 
                    session["admin"] = user.email
                    return redirect(url_for("admin_books"))
    return render_template("authentication/login.html", form=form, title="Library | Login")

# register page
@app.route("/register", methods=["GET", "POST"])
def register():
    form = Register()
    if request.method == "POST":
        # generate a salt
        salt = bcrypt.gensalt()
        # encode the string (password)
        encoded_pass = form.password.data.encode('UTF-8')
        # hash the password 
        hashed_password = bcrypt.hashpw(encoded_pass, salt)
        # create a new user object
        new_user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            address = form.address.data,
            password = hashed_password
        )
        # add and commit user to database
        db.session.add(new_user)
        db.session.commit()
        # query the db to get the generated user_id 
        user = User.query.filter_by(email=form.email.data).first()
        user_id = user.user_id
        # Also, we will create an empty record for the user to update in the future
        new_record = Record(
            user_id = user_id,
            num_books_hired = 0,
            num_books_returned = 0,
            current_num_books = 0,
        )
        # add and commit record to database
        db.session.add(new_record)
        db.session.commit()
        # account created succesfully, redirect user to login page
        return redirect(url_for("login"))
    return render_template("authentication/register.html", form=form, title="Library | Register")

# admin routes below
# initial page displays the books and has CRUD functionality
@app.route("/admin-books", methods=["GET", "POST"])
def admin_books():
    # check if the admin session variable is set 
    if "admin" in session:
        # retrieve all the books from the database and display them 
        books = Book.query.all()
        # add a book to the database when the add book button is pressed
        if request.method == 'POST':
            add_book()
            return redirect(url_for("admin_books"))
        return render_template("admin/books.html", title="Admin | Books", books=books)
    else:
        # the user is not authenticated
        return redirect(url_for("login"))

# route + function to delete a book 
@app.route("/delete-book/<book_id>", methods=["GET", "POST"])
def delete_book(book_id):
    # check if the admin session variable is set 
    if "admin" in session:
        # query to retrieve the information of the book via the book id
        book = Book.query.filter_by(book_id=book_id).first()
        # delete the book from the database
        db.session.delete(book)
        # commit the delete query
        db.session.commit()
        # flash message 
        flash("Book deleted successfully.")
        return redirect(url_for("admin_books"))       
    else:
        # the user is not authenticated
        return redirect(url_for("login"))

# route + function to update a book 
@app.route("/update-book", methods=["GET", "POST"])
def update_book():
    # check if the admin session variable is set 
    if "admin" in session:
        if request.method == "POST":
            # query to retrieve the information of the book via the book id
            book = Book.query.filter_by(book_id=request.form['book_id']).first()
            # update the information 
            book.title = request.form['title']
            book.author = request.form['author']
            book.description = request.form['description']
            book.num_of_copies = request.form['copies']
            book.description = request.form['description']
            # commit book to database
            db.session.commit()
            # flash message 
            flash("Book updated successfully.")
            return redirect(url_for("admin_books"))   
    else:
        # the user is not authenticated
        return redirect(url_for("login"))

# dispaly the reviews on the admin side
@app.route("/admin-reviews", methods=["GET", "POST"])
def admin_reviews():
    # check if the admin session variable is set 
    if "admin" in session:
        # retrieve the reviews from the database
        reviews = Review.query.all()
        # pass the reviews to the html so they can be displayed
        return render_template("admin/reviews.html", title="Admin | Reviews", reviews=reviews)
    else:
        # the user is not authenticated
        return redirect(url_for("login"))

# route + function to delete a review 
@app.route("/delete-review/<review_id>", methods=["GET", "POST"])
def delete_review(review_id):
    # check if the admin session variable is set 
    if "admin" in session:
        # query to retrieve the information of the book via the book id
        review = Review.query.filter_by(review_id=review_id).first()
        # delete the book from the database
        db.session.delete(review)
        # commit the delete query
        db.session.commit()
        # flash message 
        flash("Review deleted successfully.")
        return redirect(url_for("admin_reviews"))       
    else:
        # the user is not authenticated
        return redirect(url_for("login"))

# display the requests on the admin side
@app.route("/admin-requests", methods=["GET", "POST"])
def admin_requests():
    # check if the admin session variable is set 
    if "admin" in session:
        # retrieve the reviews from the database
        requests = Request.query.all()
        # if the add button is pressed, call the add_book() function
        if request.method == "POST":
            add_book()
            # query to retrieve the request from the db
            book_request = Request.query.filter_by(title=request.form['title']).first()
            # delete the request from the database
            db.session.delete(book_request)
            # commit the delete query
            db.session.commit()
            return redirect(url_for("admin_requests"))  
        return render_template("admin/requests.html", requests=requests, title="Admin | Requests")
    else:
        # the user is not authenticated
        return redirect(url_for("login"))

# route + function to delete a book 
@app.route("/delete-request/<request_id>", methods=["GET", "POST"])
def delete_request(request_id):
    # check if the admin session variable is set 
    if "admin" in session:
        # query to retrieve the information of the book via the book id
        request = Request.query.filter_by(request_id=request_id).first()
        # delete the book from the database
        db.session.delete(request)
        # commit the delete query
        db.session.commit()
        # flash message 
        flash("Request deleted successfully.")
        return redirect(url_for("admin_requests"))       
    else:
        # the user is not authenticated
        return redirect(url_for("login"))

# display the users on the admin side
@app.route("/admin-accounts", methods=["GET", "POST"])
def admin_accounts():
# check if the admin session variable is set 
    if "admin" in session:
        # query the database for all transactions
        transactions = Transaction.query.all()
        return render_template("admin/accounts.html", title="Admin | Accounts", transactions=transactions)
    else:
        # the user is not authenticated
        return redirect(url_for("login"))

# user routes below
# initial page displays the books with hire and review functionality
@app.route("/user-books", methods=["GET", "POST"])
def user_books():
    # check if the user session variable is set 
    if "user_id" in session:
        # retrieve all the books from the database and display them 
        books = Book.query.all()
        return render_template("user/books.html", title="Library | Books", books=books)
    else:
        # the user is not authenticated
        return redirect(url_for("login"))

# hire a book
@app.route("/hire-book/<book_id>", methods=["GET", "POST"])
def hire_book(book_id):
    # check if the user session variable is set 
    if "user_id" in session:
        user = session["user_id"]
        # check how many books the user has hired via user_id
        record = Record.query.filter_by(user_id=user).first()
        # check if the user already has this book 
        has_book = Transaction.query.filter_by(user_id=user, book_id=book_id).first()
        # query to get the books number of copies 
        book = Book.query.filter_by(book_id=book_id).first()
        num_of_copies = book.num_of_copies
        if num_of_copies <= 0:
            flash("This book is out of stock!")
            return redirect(url_for("user_books"))
        elif has_book:
            flash("You already have this book!")
            return redirect(url_for("user_books"))
        # if the user already has 3 books, refuse another   
        elif record.current_num_books == 3:
            # flash message 
            flash("You already have the maximum of three books hired!")
            return redirect(url_for("user_books"))
        else:
            # update the record 
            record.current_num_books += 1
            record.num_books_hired += 1
            db.session.commit()
            # create the issue and return date (3 months from now)
            issue_date = date.today()
            return_date = issue_date + relativedelta(months =+ 3)
            # create a transaction object
            transaction = Transaction(
                title = book.title,
                author = book.author,
                issue_date = issue_date,
                return_date = return_date,
                user_id = user,
                book_id = book_id
            )
            # add and commit transaction to database
            db.session.add(transaction)
            db.session.commit()
            # reduce the copies of the book by one
            book.num_of_copies -= 1
            db.session.commit()
            # flash message 
            flash("Book hired succesfully!")
            return redirect(url_for("user_books"))

# hire a book
@app.route("/return-book/<book_id>", methods=["GET", "POST"])
def return_book(book_id):
    # check if the user session variable is set 
    if "user_id" in session:
        user = session["user_id"]
        # remove the transaction 
        transaction = Transaction.query.filter_by(user_id=user, book_id=book_id).first()
        # delete the transaction from the database
        db.session.delete(transaction)
        # commit the delete query
        db.session.commit()
        # update the number of copies in library
        book = Book.query.filter_by(book_id=book_id).first()
        book.num_of_copies += 1
        db.session.commit()
        # update record
        record = Record.query.filter_by(user_id=user).first()
        # update the record 
        record.current_num_books -= 1
        record.num_books_returned += 1
        db.session.commit()
         # flash message 
        flash("Book returned successfully.")
        return redirect(url_for("user_account"))

# add a review 
@app.route("/add-review", methods=["GET", "POST"])
def add_review():
    # check if the user session variable is set 
    if "user_id" in session:
        user = session["user_id"]
        # create a new review object
        new_review = Review(
            user_id = user,
            title = request.form['title'],
            author = request.form['author'],
            review = request.form['review']
        )
        # add and commit book to database
        db.session.add(new_review)
        db.session.commit()
        # flash message 
        flash("Review added successfully.")
        return redirect(url_for("user_books"))
    else:
        # the user is not authenticated
        return redirect(url_for("login"))

# display the reviews on the user side
@app.route("/user-reviews", methods=["GET", "POST"])
def user_reviews():
    # check if the user session variable is set 
    if "user_id" in session:
         # retrieve the reviews from the database
        reviews = Review.query.all()
        # pass the reviews to the html so they can be displayed
        return render_template("user/reviews.html", title="Library | Reviews", reviews=reviews)
    else:
        # the user is not authenticated
        return redirect(url_for("login"))

# create a request for a book
@app.route("/user-requests", methods=["GET", "POST"])
def user_requests():
    # check if the user session variable is set 
    if "user_id" in session:
        user = session["user_id"]
        form = Requests()
        if form.validate_on_submit():
            # check if the book is already in the database 
            existing_book = Book.query.filter_by(title=form.title.data).first()
            if existing_book:
                flash("Book is already in the library!")
            else:
                # create a new request object
                new_request = Request(
                    user_id = user,
                    title = form.title.data,
                    author = form.author.data,
                    description = form.description.data
                )
                # add and commit book to database
                db.session.add(new_request)
                db.session.commit()
                # flash message 
                flash("Request sent successfully.")
                return redirect(url_for("user_requests"))
        return render_template("user/requests.html", title="Library | Requests", form=form)
    else:
        # the user is not authenticated
        return redirect(url_for("login"))

@app.route("/user-account", methods=["GET", "POST"])
def user_account():
    # check if the user session variable is set 
    if "user_id" in session:
        # query the transaction table
        transactions = Transaction.query.all()
        return render_template("user/account.html", title="Library | Account", transactions=transactions)
    else:
        # the user is not authenticated
        return redirect(url_for("login"))

# logout, remembering to remove the session variables 
@app.route("/logout")
def logout():
    # remove the user or admin from the session
    session.pop('user_id', None)
    session.pop('admin', None)
    return redirect(url_for("login"))
    