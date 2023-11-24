#!/usr/bin/env python3
"""Setup a basic Flask app
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    A class that Config available laguages in the Babel-app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def welcome():

    """A basic Flask app that creates
    a single / and an html template
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
