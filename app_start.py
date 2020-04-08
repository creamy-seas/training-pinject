"""
Entry Class
"""

from app.app_object_graph_builder import AppObjectGraphBuilder
from app.utils.binding_specs.init_details_binding_spec import InitDetailsBindingSpec
from app.utils.library_providers.config_parser.config_parser_binding_spec import ConfigParserBindingSpec

from app_manager import AppManager

class AppStart():
    @classmethod
    def run(cls, init_details):

        BINDINGSPECS = [
            InitDetailsBindingSpec(init_details),
            ConfigParserBindingSpec()
        ]

        OBJECT_GRAPH_BUILDER = AppObjectGraphBuilder()
        OBJ_GRAPH = OBJECT_GRAPH_BUILDER.get_app_object_graph(BINDINGSPECS)
        APP = OBJ_GRAPH.provide(AppManager)

        return APP

