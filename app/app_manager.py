"""
Main class that defines all the methods of the application
"""
# pylint: disable=C,E1101,R0903
import pinject


class AppManager:
    @pinject.copy_args_to_internal_fields
    def __init__(
            self,
            app_logger
    ):
        pass

    def run_print_process(self, input_text):
        self._app_logger.log(input_text)
        

