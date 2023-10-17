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

    """
    if 'locale' in request.args:
        locale = request.args['locale']
        if locale in app.config['LANGUAGES']:
            return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.init_app(app)
babel.localeselector(get_locale)


@app.route('/')
def welcome():
    """A basic Flask app that creates a single /
    and an html template...
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
