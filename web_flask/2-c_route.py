#!/usr/bin/python3

"""
    Script that starts a Flask web application.
    Web application must be listening on 0.0.0.0, port 5000.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c_test(text):
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.debug = True
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
