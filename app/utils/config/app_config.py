"""
AppConfig
"""
#pylint: disable=C

class AppConfig():
    def __init__(self, libraries_manager):
        self.config_parser = libraries_manager.config_parser.config_parser()
        self.read_config_data()

    def read_config_data(self):
        self.config_parser.read("app.conf")
        config = self.config_parser

        config_section = config["INFO-CONFIG"]
        self.data = {
            "data-print": config_section["data-print"],
            "data-integer:": int(config_section["data-integer"])
        }