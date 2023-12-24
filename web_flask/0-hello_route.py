from flask import Flask
"""0-hello_route module"""


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def display():
    """Starts a Flask web application"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(debug=True)
