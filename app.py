from flask import Flask, redirect, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
from wtforms.validators import ValidationError
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators
from wtforms.validators import InputRequired,Email, Length, ValidationError 
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'PenguinSor987@gmail.com'
app.config['MAIL_PASSWORD'] = 'Penguin_Sor123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
mail.init_app(app)



###########################     DATABASE    ###########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(40))
    lname = db.Column(db.String(40))
    email = db.Column(db.String(120))
    ph_number = db.Column(db.String(10))

    def __init__(self, fname, lname, email, ph_number):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.ph_number = ph_number
    
    def __repr__(self):
        return f"First: {self.fname}\nLast:{self.lname}\nEmail:{self.email}\nPhone:{self.ph_number}"

###########################      Forms    #############################
app.config["SECRET_KEY"] = "sekretkeylol"
class Unique(object):
    def __init__(self, model, field, message):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):         
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

class UserForm(FlaskForm):
    fname = StringField("First Name",validators=[validators.InputRequired("Please enter your first name"), validators.Length(min=1, max=40, message="The name is too long")])
    lname = StringField("Last Name",validators=[validators.InputRequired("Please enter your last name"), validators.Length(min=1, max=40, message="The last name is too long")])
    email = StringField("E-mail",validators=[validators.InputRequired("Please enter your E-mail address"), validators.Email("Enter valid E-mail address"), Unique(UserInfo, UserInfo.email, message="This email has been used for registration.")])
    ph_number = StringField("Phone Number",validators=[validators.InputRequired("Please enter your phone number"), validators.Length(min=10, max=10), Unique(UserInfo, UserInfo.ph_number, message="This phone number has been used for registration.")])
    submit = SubmitField("Submit")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/events", methods=["GET", "POST"])
def events():
    form = UserForm()
    if form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        email = form.email.data
        ph_number = form.ph_number.data
        new_user = UserInfo(fname, lname, email, ph_number)
        try:
            db.session.add(new_user)
            db.session.commit()
        except:
            return "An error occured"
        msg = Message(subject="Registration Successful.", recipients=[new_user.email], body=f"You have been successfully registered for the event.\nUser id: {new_user.id}", sender="tungaresamit@gmail.com")
        mail.send(msg)
        flash(f"Registration Successful.{new_user.id}")
        return redirect(url_for("home"))
    return render_template("events.html", form=form)

@app.route("/team")
def team():
    return "Work in progress"

@app.route("/about-us")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)