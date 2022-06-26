import os
import json
import pandas as pd

from app.utils.read_file import FileToDataframe


class GetLifeSatisfactionUseCase:
    """Life satisfaction use cases

    Returns:
        None
    """

    def index_gt(self, index_gt: float) -> list:
        """Retrive list of countries with index greater
           than user set index filter

        Arguments:
            index_gt {float} -- user set index
        Returns:
            [json] -- Cuntries list and index life satisfaction
        """

        data = FileToDataframe(os.environ['countries_file']).csv()
        data_filtered = self._filter_by(data)
        return self._make_response(data_filtered[data_filtered["Value"] > index_gt])

    def _filter_by(self, df: pd.DataFrame) -> pd.DataFrame:
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

        for filter in filters:
            df = df[df[filter["column"]] == filter["value"]]
        return df[["Country", "Value"]]

    def _make_response(self, df: pd.DataFrame) -> list:
        return json.loads(df.to_json(orient='records'))
