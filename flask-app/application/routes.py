from application import app, db
from flask import render_template, request, redirect, url_for
from application.forms import Register, Login
from application.models import User
import bcrypt

@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login()
    return render_template("login.html", form=form, title="Library | Login")


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
        return "Added user to the database!"
    return render_template("register.html", form=form, title="Library | Register")
