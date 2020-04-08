"""
Example Decorator to delay the printing
"""

#pylint: disable=C
from time import sleep
import pinject


class DelayDecorator():
    @pinject.copy_args_to_public_fields
    def __init__(self, app_logger):
        pass

    def run(self, function, input_text, seconds_to_delay):
        self.app_logger.log(f'Delaying for {seconds_to_delay}')
        sleep(seconds_to_delay)
        function(input_text)
