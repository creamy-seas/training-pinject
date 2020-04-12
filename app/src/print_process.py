"""
Class that prints to stdout
"""
# pylint: disable=C
import pinject


class PrintProcess:
    @pinject.copy_args_to_public_fields
    def __init__(self, app_logger, app_config):
        pass

    def run(self, input_text):
        print(input_text)
        self.app_logger.log("Finished Printing Process")

    def run_with_config(self):
        print(self.app_config.data["data-print"].lower())
        self.app_logger.log("Finished Printing Process")
