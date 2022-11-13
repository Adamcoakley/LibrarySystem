from application import app, db
from flask import render_template, request, redirect, url_for
from application.forms import Register, Login
from application.models import User
import bcrypt

# authentication routes
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit():
        # check if a user exists
        user = User.query.filter_by(email=form.email.data).first()
        # passwords need to be encodede to be compared
        form_pass = form.password.data.encode('UTF-8')
        user_pass = user.password.encode('UTF-8')
        if user:
            # user exists, check if their password is correct
            if bcrypt.checkpw(form_pass, user_pass):
                # password is correct, check if the user is an admin (1) or standar user (0)
                if user.is_admin == 0:
                    return redirect(url_for("user_view_books"))
                else:
                    return redirect(url_for("admin_view_books"))
    return render_template("authentication/login.html", form=form, title="Library | Login")


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
            dob = form.dob.data,
            password = hashed_password
        )
        # add and commit user to database
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        # account created succesfully, redirect user to login page
        return redirect(url_for("login"))
    return render_template("authentication/register.html", form=form, title="Library | Register")

# admin routes
@app.route("/admin-view-books", methods=["GET", "POST"])
def admin_view_books():
    return render_template("admin/books.html")

# user routes
@app.route("/user-view-books", methods=["GET", "POST"])
def user_view_books():
    return render_template("user/books.html")