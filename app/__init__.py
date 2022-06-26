"""Flask app config."""

from flask import Flask

from app.api.ping import ping_blueprint
from app.api.countries import countries_blueprint


def initialize_app(flask_app):
    """App init."""
    flask_app.register_blueprint(ping_blueprint, url_prefix="/api/v1.0")
    flask_app.register_blueprint(countries_blueprint, url_prefix="/api/v1.0")


def create_app():
    """App creation."""
    flask_app = Flask(__name__)
    initialize_app(flask_app)
    return flask_app
