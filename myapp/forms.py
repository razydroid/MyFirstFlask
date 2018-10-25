from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Email, DataRequired, Length

class SignupForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired("First Name is required")])
    lastname = StringField('Last Name', validators=[DataRequired("Last Name is required")])
    email = StringField('Email', validators=[DataRequired("Please enter a valid email"),Email("Please enter Valid Email")])
    password = PasswordField('Password', validators=[DataRequired("Password is required"),Length(min=6,message="Password must be min 6 char long")])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Please enter a valid email"),Email("Please enter Valid Email")])
    password = PasswordField('Password', validators=[DataRequired("Password is required"),Length(min=6,message="Password must be min 6 char long")])
    submit = SubmitField('Login')