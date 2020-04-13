import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock

import pandas as pd

from app.src.example_pandas_class import ExamplePandasClass


class ExamplePandasClass_Test(unittest.TestCase):
    def setUp(self):

        self.libraries_manager = Mock()
        self.libraries_manager.extlib_pandas.pandas.DataFrame = MagicMock(
            return_value=pd.DataFrame(
                {"col1": [3, 2, 1, 0], "col2": ["a", "b", "c", "d"]}
            )
        )

        self.sut = ExamplePandasClass(self.libraries_manager)

    def tearDown(default):
        pass

    def test_create_df(self):
        df = self.sut.create_df()

        self.assertTrue(
            df.equals(
                pd.DataFrame({"col1": [3, 2, 1, 0], "col2": ["a", "b", "c", "d"]})
            )
        )
        self.libraries_manager.extlib_pandas.pandas.DataFrame.assert_called()


if __name__ == "__main__":
    unittest.main()
