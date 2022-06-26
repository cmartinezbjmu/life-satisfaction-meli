"""Flask countries metrics endpoint."""
from http import HTTPStatus
from flask import request
from flask_restx import Namespace, Resource

from app.api.countries.uses_cases.get_life_satisfaction import GetLifeSatisfactionUseCase
from app.api.countries.serializers import LifeSatisfactionInputSchema

countries = Namespace("countries", description="Endpoind for get metrics by countries around of wolrd")
life_satisfaction_request = LifeSatisfactionInputSchema()


@countries.route("/life-satisfaction", methods=["POST"])
class LifeSatisfaction(Resource):
    """Process to analize life satisfaction metrics by country

    Arguments:
        Resource {Resource} -- Flask RESTPlus Resource

    Returns:
        None
    """

    def post(self) -> list:
        """Retrive list of countries based on user set index filter

        Returns:
            [json] -- Cuntries list and index life satisfaction
        """
        errors = life_satisfaction_request.validate(request.args)
        if errors:
            return str(errors), HTTPStatus.BAD_REQUEST

        index_gt = request.args.get("index_gt")
        if index_gt:
            return GetLifeSatisfactionUseCase().index_gt(float(index_gt))
