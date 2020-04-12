"""`pandas`"""

# pylint: disable=C

import pinject
import pandas


class PandasBindingSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind("pandas", to_class=PandasWrapper)


class PandasWrapper:
    def __init__(self):
        self.pandas = pandas
