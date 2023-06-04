#!/usr/bin/env python3
"""
Auth class
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Provides a template for
    implementing authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication
        is required for a given path.
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        for excluded_path in excluded_paths:
            check: List = excluded_path.split('*')
            if path.startswith(check[0]) or path + '/' == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization
        header from the request.
        """

    def authorization_header(self, request=None) -> str:
         """retrieves the value of the
         "Authorization" header from the request object
         """
         if request is None or 'Authorization' not in request.headers:
             return None
         return request.headers['Authorization']
     
     
    def current_user(self, request=None) -> TypeVar('User'):
         """Retrieves the current user"""
         return None
