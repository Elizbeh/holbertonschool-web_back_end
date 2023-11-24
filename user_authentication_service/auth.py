#!/usr/bin/env python3
""" A _hash_password method that takes in
a password string arguments and returns bytes.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


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

    @staticmethod
    def _generate_uuid() -> str:
        '''generate uuid
        '''
        new_uuid = uuid.uuid4()
        return str(new_uuid)

    def create_session(self, email: str) -> str:
        '''
        Create a new session for the user with the given email.

        Param:
        - email (str): The email address of the user.

        Returns:
        - str: The session ID generated for the user.

        Raises:
        - NoResultFound: If no user is found
        with the provided email.
        '''
        try:
            user = self._db.find_user_by(email=email)
            id = self._generate_uuid()
            self._db.update_user(user.id, session_id=id)
            return id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id):
        ''' takes a single session_id string argument and returns
        the corresponding User or None.
        '''
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id):
        '''Takes a single user_id integer as argument. Returns None.'''
        try:
            # Update the user's session_id to None
            self._db.update_user(user_id, session_id=None)
            return None
        except NoResultFound:
            # If no result is found, return None
            return None

    def get_reset_password_token(self, email: str) -> str:
        '''Reset password
        '''
        if email is None:
            return None
        try:
            user: User = self._db.find_user_by(email=email)
            id: str = _generate_uuid()
            self._db.update_user(user.id, reset_token=id)
            return id
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        '''Method to update a user's password based on a reset token.'''
        try:
            # Find the user by reset token
            user: User = self._db.find_user_by(reset_token=reset_token)
            # Hash the new password
            hashed_password: str = _hash_password(password)
            # Update the user's hashed_password and reset_token in the database
            self._db.update_user(
                    user.id, hashed_password=hashed_password, reset_token=None)
        except Exception:
            # Handle exceptions by raising a ValueError
            raise ValueError
