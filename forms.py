from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    fname = StringField("First Name")
    lname = StringField("Last Name")
    email = StringField("E-mail")
    ph_number = IntegerField("Phone Number")
    submit = SubmitField("Submit")
