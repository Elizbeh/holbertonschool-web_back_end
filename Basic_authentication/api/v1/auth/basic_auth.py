#!/usr/bin/env python3
"""
Main 0
"""
from api.v1.auth.auth import Auth
import base64
from typing import List, TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    Class BasicAuth that inherits from Auth.
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Authentication.

        Args:
            authorization_header: The value of the Authorization header.

        Returns:
            The Base64 part of the Authorization header.

        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        value = authorization_header[len("Basic "):]
        return value

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes the Base64 value of a string.

        Args:
            base64_authorization_header: The Base64 value to decode.

        Returns:
            The decoded string value.

        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode("utf-8")
            return decoded_string
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts the user email and password from the Base64 decoded value.

        Args:
            decoded_base64_authorization_header: The decoded Base64 value.

        Returns:
            A tuple containing the user email and password.

        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        string = decoded_base64_authorization_header.split(":")
        return (string[0], string[1])

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar("User"):
        """
        Retrieves the User instance based on the user email and password.

        Args:
            user_email: The user's email address.
            user_pwd: The user's password.

        Returns:
            The User instance if found, None otherwise.

        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users: List = User.search({"email": user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user

    def current_user(self, request=None) -> TypeVar("User"):
        """
        Retrieves the User instance for a given request.

        Args:
            request: The request object.

        Returns:
            The User instance associated with the request, or None if not found.

        """
        auth_header = Auth.authorization_header(self, request)
        extract = BasicAuth.extract_base64_authorization_header(self, auth_header)
        decode = BasicAuth.decode_base64_authorization_header(self, extract)
        extracted = BasicAuth.extract_user_credentials(self, decode)
        user = BasicAuth.user_object_from_credentials(self, extracted[0], extracted[1

