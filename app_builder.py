"""
Builds the full project injecting the required dependencies
Almost no changes will be needed
"""

from app.graph_builder import GraphBuilder
from app.utils.init_details.binding_specs import InitDetailsBindingSpec
from app.utils.library_providers.config_parser.config_parser_binding_spec import (
    ConfigParserBindingSpec,
)

from app_manager import AppManager


class AppBuilder:
    @classmethod
    def build(cls, init_details):

        BINDINGSPECS = [
            InitDetailsBindingSpec(init_details),
            ConfigParserBindingSpec(),
        ]

        GRAPH_BUILDER = GraphBuilder()
        OBJ_GRAPH = GRAPH_BUILDER.get_app_object_graph(BINDINGSPECS)

        # Perform the build
        APP = OBJ_GRAPH.provide(AppManager)

        return APP
