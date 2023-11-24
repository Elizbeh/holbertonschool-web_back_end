#!/usr/bin/env python3
"""Setup a basic Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale():
    """
    Determine the best-matching language
    from the supported languages.

    Uses request.accept_languages to determine the best match.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def welcome():
    """A basic Flask app that creates a single /
    and an html template...
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
