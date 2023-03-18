import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock

from app.app_manager import AppManager

class AppLogger_Tests(unittest.TestCase):
    def setUp(self):
        self.app_logger = MagicMock()
        self.app_logger.log = MagicMock()

        self.sut = AppManager(self.app_logger)

    def tearDown(default):
        pass

    def test_run_print_process(self):
        self.sut.run_print_process("123")

        self.app_logger.log.assert_called_with("123")


if __name__ == '__main__':
    unittest.main()
