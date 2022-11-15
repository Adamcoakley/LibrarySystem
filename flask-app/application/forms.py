from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, ValidationError, EqualTo
from application.models import User, Book

# register form
class Register(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired(message="This field cannot be empty.")])
    last_name = StringField("Last Name", validators=[InputRequired(message="This field cannot be empty.")])
    address = StringField("Home Address", validators=[InputRequired(message="This field cannot be empty.")])
    email = StringField("Email Address", validators=[InputRequired(message="This field cannot be empty.")])
    password = PasswordField("Password", validators=[InputRequired(message="This field cannot be empty.")])
    confirm_password = PasswordField("Confirm Password", validators=[EqualTo('password', message="Passwords must match.")])
    submit = SubmitField("Sign Up")

# login form
class Login(FlaskForm):
    email = StringField("Email Address")
    password = PasswordField("Password")
    submit = SubmitField("Sign in")

# request book form
class Requests(FlaskForm):
    title = StringField("Title",  validators=[InputRequired(message="This field cannot be empty.")])
    author = StringField("Author",  validators=[InputRequired(message="This field cannot be empty.")])
    description = TextAreaField("Description",  validators=[InputRequired(message="This field cannot be empty.")])
    submit  = SubmitField("Add Request")
