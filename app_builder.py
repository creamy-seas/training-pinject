"""
Builds the application resolving the dependency injections in `AppManager`
"""
# pylint: disable=W0613,W0611,R0201,R0903,C0103

import pinject

# Binding Specs
from app.utils.binding_specs.init_details import InitDetailsBindingSpecs

# Classes to use when resolving dependencies
from app.src.app_logger import AppLogger
from app.src.print_process import PrintProcess
from app.src.example_pandas_class import ExamplePandasClass
from app.decorators.delay_decorator import DelayDecorator
from app.utils.libraries_manager import LibrariesManager
from app.utils.external_libraries.extlib_pandas import ExtlibPandas
from app.utils.external_libraries.extlib_config_parser import ExtlibConfigParser
from app.utils.config.app_config import AppConfig

from app.app_manager import AppManager


class AppBuilder:
    """Class that resolves all the dependencies in AppManager using imports defined in this file
    """
    @classmethod
    def build(cls, init_details):
        """
        - Builds the graph of all dependecies
        - Instantiates AppManager with these dependecies
        """


        BINDINGSPECS = [
            InitDetailsBindingSpecs(init_details),
        ]

        OBJ_GRAPH = pinject.new_object_graph(binding_specs=BINDINGSPECS)

        # Perform the build
        APP = OBJ_GRAPH.provide(AppManager)

        return APP
