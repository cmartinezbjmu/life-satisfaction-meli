"""Flask api for ping response."""
from flask import Blueprint
from flask_restx import Api

from app.api.ping.views import ping

ping_blueprint = Blueprint("ping", __name__)
api_ping = Api(
    ping_blueprint,
    version="1.0",
    title="Ping",
    description="Ping"
)

api_ping.add_namespace(ping)
