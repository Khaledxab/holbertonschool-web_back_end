#!/usr/bin/env python3
"""
auth
"""

from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """
    Auth
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require_auth
        """
        if not path or not excluded_paths or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        for X_path in excluded_paths:
            if X_path[-1] == "*" and path.startswith(X_path[:-1]):
                return False
        if path in excluded_paths:
            return False
        else:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """
        authorization_header
        """
        if request:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current_user
        """
        return None

    def session_cookie(self, request=None):
        """
        session_cookie
        """
        if request is None:
            return None
        return request.cookies.get(getenv('SESSION_NAME'))
