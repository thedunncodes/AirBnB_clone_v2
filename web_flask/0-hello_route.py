#!/usr/bin/python3
"""
    A route to to return a function
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        This function returns 'Hello world'
    """
    return 'Hello HBNB!\n'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
