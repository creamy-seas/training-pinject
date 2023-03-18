"""Managing libraries for the project"""
# pylint: disable=C,R0903
import pinject

class LibrariesManager:
    @pinject.copy_args_to_public_fields
    def __init__(self, extlib_datetime):
        pass
