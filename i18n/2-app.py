#!/usr/bin/env python3
"""Setup a basic Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

babel = Babel(app)

def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.init_app(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def welcome():
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(debug=True)
