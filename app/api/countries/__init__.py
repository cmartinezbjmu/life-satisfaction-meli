"""Flask api for countries metrics."""
from flask import Blueprint
from flask_restx import Api

from app.api.countries.views import countries

countries_blueprint = Blueprint("countries-metrics", __name__)
api_process = Api(
    countries_blueprint,
    version="1.0",
    title="Countries metrics",
    description="Countries metrics endpoint",
)

api_process.add_namespace(countries)
