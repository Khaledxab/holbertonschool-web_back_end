#!/usr/bin/env python3
"""
Basic Auth
"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """[BasicAuth]
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """[summary]

            Args:
                authorization_header (str): [description]

            Returns:
                str: [description]
            """
        if not authorization_header or not isinstance(authorization_header,
                                                      str):
            return None
        if authorization_header.split(' ')[0] != 'Basic':
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        decode_base64_authorization_header
        Args:
            base64_authorization_header (str): [header]
        Returns:
            str: [decoded value of a Base64 string]
        """
        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64_authorization_header.encode('utf-8')
            return base64.b64decode(decoded).decode('utf-8')
        except Exception:
            pass

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> (str, str):
        """
        extract_user_credentials
            Returns:
                    user email and password
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        headers = decoded_base64_authorization_header.split(':')
        if headers:
            return (headers[0], headers[1])

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        user_object_from_credentials
            Returns:
                  usr instance or None
        """
        if not user_email or not user_pwd:
            return None
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if users:
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
                else:
                    return None
