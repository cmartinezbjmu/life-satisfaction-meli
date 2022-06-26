"""Countries metrics test."""
import pytest
import pandas as pd
from http import HTTPStatus
from flask.helpers import url_for

from app.api.countries.uses_cases.get_life_satisfaction import GetLifeSatisfactionUseCase

test_dataset = "test/resources/test_meli_dataset.csv"


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

    def test_get_life_satisfaction_use_case_make_response_method_valid(self):
        df = pd.read_csv(test_dataset)
        response = GetLifeSatisfactionUseCase()._make_response(df)

        assert type(response) == list
        assert response[0]["LOCATION"] == "SVN"

    def test_get_life_satisfaction_use_case_filter_by_method_valid(self):
        df = pd.read_csv(test_dataset)
        response = GetLifeSatisfactionUseCase()._filter_by(df)

        assert type(response) == pd.DataFrame
        assert response.loc[0, "Country"] == "Australia"

    def test_get_life_satisfaction_use_case_index_gt_method_valid(self, mocker):
        df = pd.read_csv(test_dataset)
        mocker.patch('app.utils.read_file.FileToDataframe.csv', return_value=df)
        response = GetLifeSatisfactionUseCase().index_gt(7)

        assert type(response) == list
        assert response[0]["Country"] == "Australia"
