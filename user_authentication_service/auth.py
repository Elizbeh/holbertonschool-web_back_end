#!/usr/bin/env python3
""" A _hash_password method that takes in
a password string arguments and returns bytes.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hashes the input password using bcrypt.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication
    database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # If the user doesn't exist, create a new user
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate user login credentials.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            # User not found, return False
            return False
        # Check if the provided pwd matches the stored hashed pwd
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)