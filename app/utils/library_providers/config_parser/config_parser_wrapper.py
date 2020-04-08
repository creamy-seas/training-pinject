"""ConfigParserWrapper"""

#pylint: disable=C
import configparser

class ConfigParserWrapper():
    def __init__(self):
        self.config_parser = configparser.ConfigParser