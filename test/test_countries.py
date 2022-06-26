"""Countries metrics test."""
from http import HTTPStatus

import pytest
from flask.helpers import url_for


class TestLifeSatisfaction(object):
    """Test suite for Life Satisfaction use case endpoint"""

    ENDPOINT = "countries-metrics.countries_life_satisfaction"

    @pytest.mark.parametrize("index", [("index_gt=7"), ("index_gt=6"), ("index_gt=9")])
    def test_post_user_set_index_gt_response_ok(self, client, index):
        response = client.post(
            f"{url_for(self.ENDPOINT)}?{index}", content_type="application/json"
        )

        assert response.status_code == HTTPStatus.OK

    @pytest.mark.parametrize("index", [("index_gt=H"), ("index_gt="), ("index_gt=*")])
    def test_post_return_400_because_no_valid_index(self, client, index):
        response = client.post(
            f"{url_for(self.ENDPOINT)}?{index}", content_type="application/json"
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json == "{'index_gt': ['Not a valid number.']}"

    @pytest.mark.parametrize("index", [("index_gt=11"), ("index_gt=-1")])
    def test_post_return_400_because_index_out_of_range(self, client, index):
        response = client.post(
            f"{url_for(self.ENDPOINT)}?{index}", content_type="application/json"
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json == "{'index_gt': ['Must be greater than or equal to 0 and less than or equal to 10.']}"

    def test_post_return_400_because_missing_index(self, client):
        response = client.post(
            f"{url_for(self.ENDPOINT)}?", content_type="application/json"
        )

        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json == "{'index_gt': ['Missing data for required field.']}"
