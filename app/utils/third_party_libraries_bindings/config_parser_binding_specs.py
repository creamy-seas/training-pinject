"""`config_parser`"""

# pylint: disable=C
import configparser
import pinject


class ConfigParserBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind("config_parser", to_class=ConfigParserWrapper)


class ConfigParserWrapper:
    def __init__(self):
        self.config_parser = configparser.ConfigParser
