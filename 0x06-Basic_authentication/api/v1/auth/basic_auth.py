#!/usr/bin/env python3
"""
Basic Auth
"""

from api.v1.auth.auth import Auth
import base64


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
