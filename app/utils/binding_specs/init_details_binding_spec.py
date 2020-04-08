"""
Bind the init_details dictionary to an instance
"""

#pylint: disable=C
import pinject

class InitDetailsBindingSpec(pinject.BindingSpec):
    def __init__(self, init_details):
        self.init_details = init_details

    def configure(self, bind):
        bind("init_details", to_instance=self.init_details)