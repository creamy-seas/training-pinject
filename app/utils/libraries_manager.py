"""
Managing the third party libraries e.g. selenium, config parser
"""

import pinject


class LibrariesManager:
    @pinject.copy_args_to_public_fields
    def __init__(self, extlib_config_parser, extlib_pandas):
        pass
