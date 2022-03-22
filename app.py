from flask import Flask, redirect, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os
from forms import UserForm

app = Flask(__name__)

###########################     DATABASE    ###########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

###########################      Forms    #############################
app.config["SECRET_KEY"] = "sekretkeylol"

class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(40))
    lname = db.Column(db.String(40))
    email = db.Column(db.String(120))
    ph_number = db.Column(db.Integer)

    def __init__(self, fname, lname, email, ph_number):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.ph_number = ph_number
    
    def __repr__(self):
        return f"First: {self.fname}\nLast:{self.lname}\nEmail:{self.email}\nPhone:{self.ph_number}"

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
        db.session.add(new_user)
        db.session.commit()
        flash(f"User registered id: {new_user.id}")
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