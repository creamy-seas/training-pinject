import unittest
from unittest.mock import Mock
from unittest.mock import MagicMock

from app.src.app_logger import AppLogger

class AppLogger_Tests(unittest.TestCase):
    def setUp(self):
        self.libraries_manager = MagicMock()
        self.libraries_manager.extlib_datetime.datetime.now().strftime.return_value = "2020-01-01 23:59:59.00"

        self.sut = AppLogger(self.libraries_manager)

    def tearDown(default):
        pass

    def test_log(self):
        self.sut.log("123")

        self.libraries_manager.extlib_datetime.datetime.now.assert_called_with()
        self.libraries_manager.extlib_datetime.datetime.now().strftime.assert_called()


if __name__ == '__main__':
    unittest.main()
