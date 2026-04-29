import time

class TimeManager:
    def __init__(self):
        self.offset = 0

    def set_timezone(self, offset):
        self.offset = offset

    def get_time(self):
        current = time.localtime()
        hour = (current.tm_hour + self.offset) % 24
        return hour, current.tm_min, current.tm_sec