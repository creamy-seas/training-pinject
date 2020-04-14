"""Library for parsing configuration files"""
# pylint: disable=R0903
import configparser


class ExtlibConfigParser:
    def __init__(self):
        self.config_parser = configparser.ConfigParser
