#!/usr/bin/env python3
""" Module of Session in Database
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ Session DB Auth class """
    def create_session(self, user_id: str = None) -> str:
        """ creates a Session ID for a user_id """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_id = self.user_id_by_session_id[session_id]
        session_dictionary = {
            'user_id': user_id,
            'session_id': session_id
        }
        user_session = UserSession(**session_dictionary)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ returns a User ID based on a Session ID """
        if session_id is None:
            return None
        try:
            user_session = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if not user_session:
            return None
        user_session = user_session[0]
        if self.session_duration <= 0:
            return user_session.user_id
        if user_session.created_at + timedelta(seconds=self.session_duration) < datetime.now():
            return None
        return user_session.user_id

    def destroy_session(self, request=None):
        """ deletes the user session / logout """
        if request is None:
            return False
        cookie = self.session_cookie(request)
        if cookie is None:
            return False
        user_id = self.user_id_for_session_id(cookie)
        if user_id is None:
            return False
        try:
            user_session = UserSession.search({'session_id': cookie})
        except Exception:
            return False
        if not user_session:
            return False
        user_session = user_session[0]
        user_session.remove()
        return True

    def get_user_from_session_id(self, session_id: str = None) -> str:
        """ returns a User instance based on a cookie value """
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)

    def create_session(self, user_id: str = None) -> str:
        """ creates a Session ID for a user_id """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_id = self.user_id_by_session_id[session_id]
        session_dictionary = {
            'user_id': user_id,
            'session_id': session_id
        }
        user_session = UserSession(**session_dictionary)
        user_session.save()
        return session_id
