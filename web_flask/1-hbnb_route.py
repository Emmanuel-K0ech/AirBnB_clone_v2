#!/usr/bin/python3
""" Route /hbtn"""
from flask import Flask
app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Function Displaying the text on screen """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
