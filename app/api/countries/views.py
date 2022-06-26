"""Flask countries metrics endpoint."""
from flask import request
from flask_restx import Namespace, Resource

from app.api.countries.uses_cases.get_life_satisfaction import GetLifeSatisfactionUseCase

countries = Namespace("countries", description="Endpoind for get metrics by countries around of wolrd")


@countries.route("/life-satisfaction", methods=["POST"])
class LifeSatisfaction(Resource):
    """Process to analize life satisfaction metrics by country

    Arguments:
        Resource {Resource} -- Flask RESTPlus Resource

    Returns:
        None
    """

    def post(self):
        """Retrive list of countries based on user set index filter

        Returns:
            [json] -- Cuntries list and index life satisfaction
        """
        args = request.args
        index_gt = args.get("index[gt]")

        if index_gt:
            return GetLifeSatisfactionUseCase().index_gt(float(index_gt))
