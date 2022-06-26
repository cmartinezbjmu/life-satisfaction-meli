import os
import json
import pandas as pd

from app.utils.read_file import FileToDataframe


class GetLifeSatisfactionUseCase:
    """Life satisfaction use cases

    Returns:
        None
    """

    def index_gt(self, index_gt):
        """Retrive list of countries with index greater
           than user set index filter

        Arguments:
            index_gt {float} -- user set index
        Returns:
            [json] -- Cuntries list and index life satisfaction
        """
        # Use case columns filter values
        filters = [
            {
                "column": "INDICATOR",
                "value": "SW_LIFS",
            },
            {
                "column": "INEQUALITY",
                "value": "TOT",
            }
        ]
        data = FileToDataframe(os.environ['countries_file']).csv()
        data_filtered = self.filter_by(data, filters)
        return self._make_response(data_filtered[data_filtered["Value"] > index_gt])

    def filter_by(self, df: pd.DataFrame, filters: list) -> pd.DataFrame:

        for filter in filters:
            df = df[df[filter["column"]] == filter["value"]]
        return df[["Country", "Value"]]

    def _make_response(self, df: pd.DataFrame):
        return json.loads(df.to_json(orient='records'))
