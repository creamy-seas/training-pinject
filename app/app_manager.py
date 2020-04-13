"""
File that exposes/defines all the methods of the application
"""
# pylint: disable=W0613,W0611,R0201
import pinject


class AppManager:
    @pinject.copy_args_to_internal_fields
    def __init__(
        self,
        init_details,
        app_logger,
        print_process,
        delay_decorator,
        example_pandas_class,
    ):
        pass

    def run_print_process(self, input_text):
        self._app_logger.log("Start Printing Text")
        self._print_process.run(input_text)

    def run_print_process_with_init(self):
        self._app_logger.log("Start Printing Text")
        self._print_process.run(self._init_details)

    def run_print_process_with_delay(self, input_text, seconds_to_delay):
        # decorator example
        self._app_logger.log("Start Printing Text with Delay")
        self._delay_decorator.run(self._print_process.run, input_text, seconds_to_delay)

    def run_print_process_with_config(self):
        self._app_logger.log("Start Printing Text with Config")
        self._print_process.run_with_config()

    def run_example_pandas(self):
        df = self._example_pandas_class.create_df()
        self._example_pandas_class.print_df(df)
