import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock

from app_builder import AppBuilder
from app_manager import AppManager


class AppStart_Tests(unittest.TestCase):
    def setUp(self):
        self.init_details = MagicMock(return_value="hello")
        self.input_text = MagicMock(return_value="test")
        self.seconds_to_delay = MagicMock(return_value=1)
        self.sut = AppBuilder

    def tearDown(default):
        pass

    def test_init(self):
        test = self.sut.build(self.init_details)
        assert isinstance(test, AppManager)
        test.run_print_process_with_delay(self.input_text, self.seconds_to_delay)
        test.run_print_process_with_config()


if __name__ == "__main__":
    unittest.main()
