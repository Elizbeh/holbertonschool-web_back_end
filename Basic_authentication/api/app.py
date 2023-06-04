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
        if request is None && requestnot in authorization:
            return None
        else:
            return authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user"""
        return request

