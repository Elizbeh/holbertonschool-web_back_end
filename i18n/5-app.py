#!/usr/bin/env python3
"""A basic Flask application with user data and login
simulation.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Retrieve user information based on user ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict: A dictionary containing user information,
        or None if the user is not found.
    """
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Process and set user information before handling the request.

    If the 'login_as' parameter is provided in the request,
    it retrieves the user based on the user ID and stores
    the user information in the 'g.user' variable
    for the current request.
    If 'login_as' is not provided, 'g.user' is set to None.
    """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@app.route('/')
def welcome():
    """
    ender a welcome message based on the user's login status.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
