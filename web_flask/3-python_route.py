#!/usr/bin/python3
""" Route /c/<text>"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ C Hello """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ <text>: hbnb """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def ctext(text):
    """ displays C followed by value of <text> """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pytext(text="is cool"):
    """ displays 'Python' followed by text in variable <text> """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
