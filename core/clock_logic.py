import math

class ClockLogic:

    @staticmethod
    def get_angles(hour, minute, second):
        h = math.radians((hour % 12) * 30 + minute * 0.5 - 90)
        m = math.radians(minute * 6 + second * 0.1 - 90)
        s = math.radians(second * 6 - 90)
        return h, m, s