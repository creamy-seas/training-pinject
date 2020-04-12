"""
Example class showing how 3rd party library is used
"""

import pinject


class ExamplePandasClass:
    @pinject.copy_args_to_public_fields
    def __init__(self, libraries_manager):
        self.pandas = libraries_manager.pandas.pandas

    def create_df(self) -> "DataFrame":
        data = {"col_1": [3, 2, 1, 0], "col_2": ["a", "b", "c", "d"]}
        return self.pandas.DataFrame.from_dict(data)

    def print_df(self, df: "DataFrame"):
        print(df)
