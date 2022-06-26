"""Flask app config."""

from flask import Flask

from app.api.ping import ping_blueprint


def initialize_app(flask_app):
    """App init."""
    flask_app.register_blueprint(ping_blueprint)

def create_app():
    """App creation."""
    flask_app = Flask(__name__)
    initialize_app(flask_app)
    return flask_app
