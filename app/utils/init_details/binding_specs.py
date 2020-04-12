"""
Class to build the app with some initial details passed in as arguments
"""

# pylint: disable=C
import pinject


class InitDetailsBindingSpec(pinject.BindingSpec):
    def __init__(self, user_init_details):
        self.init_details = user_init_details

    def configure(self, bind):
        bind("init_details", to_instance=self.init_details)
