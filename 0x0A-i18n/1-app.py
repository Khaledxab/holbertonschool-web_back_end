#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):

    LANGUAGES = ["en", "fr"]

    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
"""use config class for flask"""


@app.route('/')
def root():
    """ Root route """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
