"""Utils test."""
import pandas as pd
from app.utils.read_file import FileToDataframe

test_dataset = "test/resources/test_meli_dataset.csv"


class TestUtils(object):
    """Test suite for utils"""

    def test_get_life_satisfaction_use_case_index_gt_method_valid(self, mocker):
        df = pd.read_csv(test_dataset)
        mocker.patch('app.utils.read_file.FileToDataframe.csv', return_value=df)
        response = FileToDataframe("test").csv()

        assert type(response) == pd.DataFrame

    def test_get_life_satisfaction_use_case_index_gt_method_invalid(self, mocker):
        response = FileToDataframe("test").csv()

        assert response == None
