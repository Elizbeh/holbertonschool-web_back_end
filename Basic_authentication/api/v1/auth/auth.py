#!/usr/bin/env python3
""" Class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ A class to manage the API authentication.
    """
    def require_auth(self, path: str,
                     excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the
        given path.

        Args:
            path (str): The path of the request.
            excluded_paths (List[str]): List of paths
            excluded from authentication.

        Returns:
            bool: True if authentication is required,
            False otherwise.
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        for i in excluded_paths:
            check: List = i.split('*')
            if path.startswith(check[0]) or path + '/' == i:
                return False
            return True

    def authorization_header(self, request=None) -> str:
        """
        Placeholder for obtaining the authorization header.

        :param request: Flask request object.
        :return: None for now.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder for obtaining the current user.

        :param request: Flask request object.
        :return: None for now.
        """
        return None
