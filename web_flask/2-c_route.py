#!/usr/bin/python3
"""2-c_route module"""
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """/c/<text>: display C the text"""
    text_written = "{}".format(text)
    new_text_written = text_written.replace('_', ' ')

    return "C {}".format(new_text_written)


if __name__ == '__main__':
    app.run(debug=True)
