"""Logger"""
from datetime import datetime

class AppLogger():
    def __init__(self):
        pass

    def log(self, log_string):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print(time + " - " + log_string)