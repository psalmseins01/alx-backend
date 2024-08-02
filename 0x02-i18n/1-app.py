#!/usr/bin/env python3
"""
Basic flask app setup
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiation of application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrapping the application with Babel
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Basic html template rendering
    """
    return render_template('1-index.html')
