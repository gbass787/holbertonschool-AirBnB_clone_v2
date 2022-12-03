#!/usr/bin/python3
"""
    Script that starts a Flask web application.
    Web application must be listening on 0.0.0.0, port 5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_test(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('/5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):

    if isinstance(n, int):
        if n % 2 == 0:
            ans = "even"
        else:
            ans = "odd"

        return render_template('/6-number_odd_or_even.html', n=n, evenodd=ans)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
