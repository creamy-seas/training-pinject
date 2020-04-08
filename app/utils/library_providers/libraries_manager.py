"""
Managing the third party libraries e.g. selenium, config parser
"""

# if using pylint disable the too many arguements rule
# pylint: disable=R

import pinject

class LibrariesManager():
    @pinject.copy_args_to_public_fields
    def __init__(self, config_parser):
        pass