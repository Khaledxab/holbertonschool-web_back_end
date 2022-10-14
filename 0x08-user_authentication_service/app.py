#!/usr/bin/env python3
""" Basic Flask app, Register user, Log in, Log out, User profile,
    Get reset passwords token, Update password end-point """
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome():
    """ Basic Flask app, return a JSON """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """ Register user, takes an email and password string arguments and
        returns a JSON payload """
    email = request.form.get('email')
    pwd = request.form.get('password')
    try:
        AUTH.register_user(email, pwd)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """ Log in, takes an email and password string arguments and returns a
        JSON payload """
    email = request.form.get('email')
    pwd = request.form.get('password')
    if AUTH.valid_login(email, pwd):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """ Log out, takes a cookie value from the request and returns a JSON
        payload """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """ User profile, takes a cookie value from the request and returns a
        JSON payload """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """ Get reset passwords token, takes an email string argument and returns
        a JSON payload """
    email = request.form.get('email')
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """ Update password end-point, takes an email and reset_token string
        arguments and returns a JSON payload """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_pwd = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, new_pwd)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
