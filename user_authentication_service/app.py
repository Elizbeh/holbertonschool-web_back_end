#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, jsonify, request, abort, make_response, redirect

from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def Bienvenue():
    """
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_user():
    """
    """
    try:
        email = request.form.get("email")
        password = request.form.get("password")

        user = AUTH.register_user(email, password)

        return jsonify({"email": user.email, "message": "user created"}), 200

    except ValueError as e:
        return jsonify({"message": str(e)}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    ''' POST on session
    '''
    email: str = request.form.get('email')
    password: str = request.form.get('password')
    if not email or not password:
        return abort(401)

    check: bool = AUTH.valid_login(email=email, password=password)
    if not check:
        abort(401)

    session_id: str = AUTH.create_session(email=email)
    response = jsonify(email=email, message='logged in')
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    '''Logout function to handle DELETE /sessions route.'''
    session_id = request.cookies.get('session_id')

    if session_id is None:
        # If session_id is not provided, respond with 403 status
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        # If user does not exist, respond with 403 status
        abort(403)

    # Destroy the session
    AUTH.destroy_session(user.id)

    # Redirect the user to GET /
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
