"""Flask ping endpoint."""
from flask import make_response
from flask_restx import Namespace, Resource

ping = Namespace("ping", description="Ping pong endpoint")


@ping.route("/")
class Ping(Resource):
    """Ping."""

    def get(self):
        """Ping pong.

        Just returns pong in text/plain
        """
        response = make_response("pong")
        response.headers["content-type"] = "text/plain"
        return response
