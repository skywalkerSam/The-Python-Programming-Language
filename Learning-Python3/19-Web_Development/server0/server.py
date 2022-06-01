# Web server for Server-ZERO.

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/about")
def about():
    return "<h1>About: This is Server-ZERO (Experinmental) </h1>"


@app.route("/contact")
def contact():
    return "<h1>Contact: Server-ZERO by @skywalkerSam </h1>"
