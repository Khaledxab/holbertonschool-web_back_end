#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup, Get locale from request,
    Parametrize templates, Force locale with URL parameter, Mock logging in,
    Use user locale """
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

Users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def root():
    """ Root route """
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """ Get locale from request """
    locale = request.args.get('locale')
    supportLang = app.config['LANGUAGES']
    if locale in supportLang:
        return locale
    userId = request.args.get('login_as')
    if userId:
        locale = users[int(userId)]['locale']
        if locale in supportLang:
            return locale
    locale = request.headers.get('locale')
    if locale in supportLang:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """ Get user from request """
    if 'login_as' in request.args:
        user_id = int(request.args.get('login_as'))
        if user_id in Users:
            return Users[user_id]

    
@app.before_request
def before_request():
    """ Before reqsuest """
    user = get_user()
    if user:
        g.user = user


if __name__ == "__main__":
    app.run()