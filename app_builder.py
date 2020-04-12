"""
Builds the application resolving the dependency injections in `AppManager`
"""
# pylint: disable=W0613,W0611,R0201

import pinject

# Binding Specs
from app.utils.internal_bindings.init_details import InitDetailsBindingSpec
from app.utils.third_party_libraries_bindings.config_parser_binding_specs import (
    ConfigParserBindingSpec,
)
from app.utils.third_party_libraries_bindings.pandas_binding_specs import (
    PandasBindingSpec,
)

# Dependecy Injection Classes
from app.src.app_logger import AppLogger
from app.src.print_process import PrintProcess
from app.src.example_pandas_class import ExamplePandasClass

from app.decorators.delay_decorator import DelayDecorator

from app.utils.libraries_manager import LibrariesManager
from app.utils.config.app_config import AppConfig

from app_manager import AppManager


class AppBuilder:
    @classmethod
    def build(cls, init_details):

        BINDINGSPECS = [
            InitDetailsBindingSpec(init_details),
            ConfigParserBindingSpec(),
            PandasBindingSpec(),
        ]

        OBJ_GRAPH = pinject.new_object_graph(binding_specs=BINDINGSPECS)

        # Perform the build
        APP = OBJ_GRAPH.provide(AppManager)

        return APP
