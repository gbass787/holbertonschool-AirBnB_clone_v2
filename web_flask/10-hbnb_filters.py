#!/usr/bin/python3
"""
    Script that starts a Flask web application.
    Web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)

@app.teardown_appcontext
def teardown(ext):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
