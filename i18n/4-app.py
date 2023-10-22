#!/usr/bin/env python3

"""Setup a basic Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    A class that Config available languages in the Babel-app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def welcome():
    """A basic Flask app that creates a single /
    and an HTML template...
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """
    Determine the best-matching language from the supported languages.

    Uses request.accept_languages to determine the best match.
    """
    if 'locale' in request.args:
        locale = request.args['locale']
        if locale in app.config['LANGUAGES']:
            return locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
