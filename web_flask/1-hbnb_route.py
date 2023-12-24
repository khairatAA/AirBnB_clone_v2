#!/usr/bin/python3
"""1-hbnb_route module"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """/: display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/hbnb: display “HBNB”"""
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True)
