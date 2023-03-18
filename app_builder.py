"""
Builds the application resolving all the dependencies
"""

import pinject

from app.src.app_logger import AppLogger
from app.utils.libraries_manager import LibrariesManager
from app.utils.external_libraries.extlib_datetime import ExtlibDatetime
from app.app_manager import AppManager

class AppBuilder:
    
    @classmethod
    def build(cls):

        OBJ_GRAPH = pinject.new_object_graph()
        APP = OBJ_GRAPH.provide(AppManager)

        return APP
