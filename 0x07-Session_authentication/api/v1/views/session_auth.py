#!/usr/bin/env python3
""" handles all routes for the views for Session authentication """
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login """
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    try:
        users = User.search({'email': email})
    except Exception:
        return None
    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            output = jsonify(user.to_json())
            session_name = getenv('SESSION_NAME')
            output.set_cookie(session_name, session_id)
            return output
    return jsonify({"error": "no user found for this email"}), 404
