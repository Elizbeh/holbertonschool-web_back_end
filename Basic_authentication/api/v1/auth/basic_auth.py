#!/usr/bin/env python3
""" Main 0
"""
from api.v1.auth.auth import Auth
import base64
from typing import List, TypeVar
from models.user import User


class BasicAuth(Auth):
    """Class BasicAuth that inherits from Auth.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        '''returns the Base64 part of the Authorization header for a
        Basic Authentication:
        '''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        value = authorization_header[len('Basic '):]
        return value

    def decode_base64_authorization_header(
                                           self, base64_authorization_header:
                                           str) -> str:
        ''' returns the decoded value of a Base64 string
        base64_authorization_header:
        '''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except (base64.binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
                                 self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        '''
        returns the user email and password from the Base64 decoded value.
        '''
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        string = decoded_base64_authorization_header.split(":")
        return(string[0], string[1])

    def user_object_from_credentials(
                                     self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        ''' returns the User instance based on his email and password.
        '''
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

    def current_user(self, request=None) -> TypeVar('User'):
        '''overloads Auth and retrieves the User instance for a request
        '''
        auth_header = Auth.authorization_header(self, request)
        extract = BasicAuth.extract_base64_authorization_header(self,
                                                                auth_header)
        decode = BasicAuth.decode_base64_authorization_header(self, extract)
        extracted = BasicAuth.extract_user_credentials(self, decode)
        user = BasicAuth.user_object_from_credentials(self, extracted[0],
                                                      extracted[1])
        return user
