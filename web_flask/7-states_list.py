#!/usr/bin/python3
"""Script that starts a Flask web application"""

import sys
from flask import Flask, render_template
sys.path.append('/home/osvaldo_jose1/holbertonschool-AirBnB_clone_v2')
from models import storage
from models.state import State

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


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
