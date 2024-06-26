#!/usr/bin/python3
"""Script that starts a Flask web application"""

import sys
sys.path.append('/home/osvaldo_jose1/holbertonschool-AirBnB_clone_v2')
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """Render state_list.html"""
    states = storage.all(State)
    states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def display_cities():
    states = storage.all(State)
    states = sorted(states.values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states():
    states = storage.all(State).values()
    if id:
        for state in states:
            if state.id == id:
                return render_template('9-states.html', states=states)
        return ("Not Found")
    else:
        return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.errorhandler(404)
def not_found_error(e):
    return render_template('error.html', status_msg = str(e)), 404


@app.route('/hbnb_filters')
def display_filter_search():

    states = storage.all(State)
    states = sorted(states.values(), key=lambda state: state.name)

    amenities = storage.all(Amenity).values()
    for amenity in amenities:
        print(f"-{amenity.name}-")

    return render_template('10-hbnb_filters.html', states = states, amenities = amenities)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
