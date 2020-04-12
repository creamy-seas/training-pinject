"""
Class that loads configuration from file `app.conf`
"""
# pylint: disable=C


class AppConfig:
    def __init__(self, libraries_manager):
        self.config_parser = libraries_manager.config_parser.config_parser()
        self.read_config_data()

    def read_config_data(self):
        self.config_parser.read("app.conf")

        self.data = {
            "data-print": self.config_parser["INFO-CONFIG"]["data-print"],
            "data-integer:": int(self.config_parser["INFO-CONFIG"]["data-integer"]),
        }
