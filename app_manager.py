"""
File that exposes/defines all the methods that can be called by the application
"""

#pylint: disable=C
import pinject

class AppManager():
    @pinject.copy_args_to_public_fields
    def __init__ (self, init_details, app_logger, print_process, delay_decorator):
        pass

    def run_print_process(self, input_text):
        self.app_logger.log('Start Printing Text')
        self.print_process.run(input_text)

    def run_print_process_with_init(self):
        self.app_logger.log('Start Printing Text')
        self.print_process.run(self.init_details)

    def run_print_process_with_delay(self, input_text, seconds_to_delay):
        #decorator example
        self.app_logger.log('Start Printing Text with Delay')
        self.delay_decorator.run(self.print_process.run, input_text, seconds_to_delay)
    
    def run_print_process_with_config(self):
        self.app_logger.log('Start Printing Text with Config')
        self.print_process.run_with_config()
