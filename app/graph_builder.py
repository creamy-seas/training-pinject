"""
Import all modules (i.e. classes and functions) used in the project
"""
# disabling unused import rule:
# pylint: disable=W0613,W0611,R0201

import pinject

from app.src.app_logger import AppLogger
from app.src.print_process import PrintProcess

from app.decorators.delay_decorator import DelayDecorator

from app.utils.library_providers.libraries_manager import LibrariesManager
from app.utils.config.app_config import AppConfig


class GraphBuilder:
    def get_app_object_graph(self, binding_specs):
        return pinject.new_object_graph(binding_specs=binding_specs)
