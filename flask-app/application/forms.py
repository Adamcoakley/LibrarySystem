from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField
from wtforms.validators import InputRequired, ValidationError, EqualTo
from application.models import User

class Register(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired(message="This field cannot be empty.")])
    last_name = StringField("Last Name", validators=[InputRequired(message="This field cannot be empty.")])
    address = StringField("Home Address", validators=[InputRequired(message="This field cannot be empty.")])
    dob = DateField("Date of Birth", validators=[InputRequired(message="This field cannot be empty.")])
    email = StringField("Email Address", validators=[InputRequired(message="This field cannot be empty.")])
    password = PasswordField("Password", validators=[InputRequired(message="This field cannot be empty.")])
    confirm_password = PasswordField("Confirm Password", validators=[EqualTo('password', message="Passwords must match.")])
    submit = SubmitField("Sign Up")

    def validate_email(self, email):
        existing_user = User.query.filter_by(email=email.data).first()

        if existing_user:
            raise ValidationError("That email is already in use. Please use a different one.")

class Login(FlaskForm):
    email = StringField("Email Address")
    password = PasswordField("Password")
    submit = SubmitField("Sign in")