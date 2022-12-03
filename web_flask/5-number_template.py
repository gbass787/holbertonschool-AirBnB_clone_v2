#!/usr/bin/python3
"""
    Script that starts a Flask web application.
    Web application must be listening on 0.0.0.0, port 5000
"""


from flask import Flask, render_template

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


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    if isinstance(n, int):
        return render_template('/5-number.html', n=n)


if __name__ == "__main__":
    app.debug = True
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
