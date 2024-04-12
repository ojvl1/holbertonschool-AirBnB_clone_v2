#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    state = storage.all()
    return render_template('7-states_list.html', state=state)


@app.teardown_appcontext('/states_list')
def teardown(exception):
    """Remove SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
