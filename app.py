from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/events")
def events():
    return "Work in progress"

@app.route("/team")
def team():
    return "Work in progress"

@app.route("/about-us")
def about():
    return "Work in progress"

@app.route("/recruitment")
def recruitment():
    return "Work in progress"

if __name__ == "__main__":
    app.run(debug=True)