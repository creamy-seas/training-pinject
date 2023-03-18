"""
Class that print timestamp and custom message to sdout
"""
# pylint: disable=C,R0903
import pinject

class AppLogger():

    @pinject.copy_args_to_public_fields
    def __init__(self,
               libraries_manager,
    ):
        self.datetime = libraries_manager.extlib_datetime.datetime

    def log(self, log_string):
        time = self.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f"{time} - {log_string}")
        

