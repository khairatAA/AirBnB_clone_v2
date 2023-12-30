#!/usr/bin/python3
"""hbnb_filters module"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb: display a HTML with content of the airbnb clone dynamically"""
    state_obj = storage.all(State)
    city_obj = storage.all(City)
    amenity_obj = storage.all(Amenity)
    place_obj = storage.all(Place)

    return render_template(
        '100-hbnb.html',
        state_obj=state_obj,
        city_obj=city_obj,
        amenity_obj=amenity_obj,
        place_obj=place_obj,
        )


@app.teardown_appcontext
def teardown_db(exception):
    """To remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
