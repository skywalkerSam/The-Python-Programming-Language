
# Read the documentation for any queries or problems...



from flask import Flask

app = Flask(__name__)
print(__name__)


@app.route("/")
def hello_skywalker():
    return "<p>Hello, Capt.Skywalker!</p>"





