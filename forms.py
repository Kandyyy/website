from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired,Email, Length, ValidationError

class UserForm(FlaskForm):
    fname = StringField("First Name", [InputRequired("Please enter your first name"), Length(min=1, max=40, message="The name is too long")])
    lname = StringField("Last Name", [InputRequired("Please enter your last name"), Length(min=1, max=40, message="The last name is too long")])
    email = StringField("E-mail", [InputRequired("Please enter your E-mail address"), Email("Enter valid E-mail address")])
    ph_number = StringField("Phone Number", [InputRequired("Please enter your phone number"), Length(min=10, max=10)])
    submit = SubmitField("Submit")
