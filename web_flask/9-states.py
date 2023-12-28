#!/usr/bin/python3
"""7-states_list module"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """states: display a HTML with the state name and id"""
    state_obj = storage.all(State)
    city_obj = storage.all(City)

    if "State.{}".format(state_id) in state_obj:
        state = state_obj["State.{}".format(state_id)]
        return render_template(
            '9-states.html',
            state_obj=state_obj,
            state_id=state_id,
            city_obj=city_obj,
            state=state
            )
    return render_template(
            '9-states.html',
            state_obj=state_obj,
            state_id=state_id,
            city_obj=city_obj,
            )


@app.teardown_appcontext
def teardown_db(exception):
    """To remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
