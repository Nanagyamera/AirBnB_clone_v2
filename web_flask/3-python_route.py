#!/usr/bin/python3
"""script to start a flaskweb  application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """specific routing"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def dynamic_text(text=None):
    """dynamic routing"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_dynamic(text='is_cool'):
    """dynamic w/ defaults"""
    return "Python {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
