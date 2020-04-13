import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock

import pandas as pd

from app.app_manager import AppManager


class AppManager_Tests(unittest.TestCase):
    def setUp(self):
        self.init_details = MagicMock(return_value="hello")

        self.app_logger = Mock()
        self.app_logger.log = Mock()

        self.print_process = Mock()
        self.print_process.run = Mock()
        self.print_process.run_with_config = Mock()

        self.delay_decorator = Mock()
        self.delay_decorator.run = Mock()

        self.example_pandas_class = Mock()
        self.example_pandas_class.create_df = MagicMock(
            return_value=pd.DataFrame(
                {"col1": [3, 2, 1, 0], "col2": ["a", "b", "c", "d"]}
            )
        )
        self.example_pandas_class.print_df = Mock()

        self.sut = AppManager(
            self.init_details,
            self.app_logger,
            self.print_process,
            self.delay_decorator,
            self.example_pandas_class,
        )

    def tearDown(default):
        pass

    def test_run_print_process(self):
        input_text = "Moo"

        self.sut.run_print_process(input_text)

        self.app_logger.log.assert_called_with("Start Printing Text")
        self.print_process.run.assert_called_with(input_text)

    def test_run_print_process_with_init(self):

        self.sut.run_print_process_with_init()

        self.app_logger.log.assert_called_with("Start Printing Text")
        self.print_process.run.assert_called_with(self.init_details)

    def test_run_print_process_with_delay(self):
        input_text = "Ted"
        seconds_to_delay = 2

        self.sut.run_print_process_with_delay(input_text, seconds_to_delay)

        self.app_logger.log.assert_called_with("Start Printing Text with Delay")
        self.delay_decorator.run.assert_called_with(
            self.print_process.run, input_text, seconds_to_delay
        )

    def test_run_print_process_with_config(self):
        input_text = "Ted"
        seconds_to_delay = 2

        self.sut.run_print_process_with_config()

        self.app_logger.log.assert_called_with("Start Printing Text with Config")
        self.print_process.run_with_config.assert_called_with()

    def test_run_example_pandas(self):

        self.sut.run_example_pandas()

        self.example_pandas_class.create_df.assert_called_with()
        self.example_pandas_class.print_df.assert_called()


#     def test_init(self):
#         test = self.sut.build(self.init_details)
#         assert isinstance(test, AppManager)
#         test.run_print_process_with_delay(self.input_text, self.seconds_to_delay)
#         test.run_print_process_with_config()


# if __name__ == "__main__":
#     unittest.main()
