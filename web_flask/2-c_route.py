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


@app.route("/c/is_fun", strict_slashes=False)
def ctext():
    """ C text """
    return "C is fun"


@app.route("/c/cool", strict_slashes=False)
def ctext2():
    """ Second C Text """
    return "C cool"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
