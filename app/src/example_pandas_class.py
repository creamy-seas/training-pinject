"""
Example class showing how 3rd party library is used
"""
# pylint: disable
import pinject


class ExamplePandasClass:
    """Class showing usage of a 3rd party library"""
    @pinject.copy_args_to_public_fields
    def __init__(self, libraries_manager):
        self.pandas = libraries_manager.extlib_pandas.pandas

    def create_df(self) -> "DataFrame":
        dataframe = self.pandas.DataFrame({"col_1": [3, 2, 1, 0], "col_2": ["a", "b", "c", "d"]})
        return dataframe

    def print_df(self, df: "DataFrame"):
        print(df)
