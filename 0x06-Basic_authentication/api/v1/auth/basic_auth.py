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
