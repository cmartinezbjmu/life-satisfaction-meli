"""Read files and transform to Pandas Dataframe."""
import pandas as pd
from app.settings import STATIC_ROOT


class FileToDataframe:
    """Read files and transform to dataframe.

    Arguments:
        filename {str} -- Filename to transform
        sep {str} -- Delimiter to use, default ','
    Returns:
        None
    """

    def __init__(self, filename: str, sep: str = ",") -> None:
        self.filename = filename
        self.sep = sep

    def csv(self) -> pd.DataFrame:
        """Transform CSV file to dataframe.

        Arguments:
            none

        Returns:
            Dataframe {dataframe} -- Pandas Dataframe
        """
        try:
            return pd.read_csv(f"{STATIC_ROOT}/csv/{self.filename}.csv", sep=self.sep)
        except FileNotFoundError:
            print("File not found.")
        except pd.errors.EmptyDataError:
            print("No data")
