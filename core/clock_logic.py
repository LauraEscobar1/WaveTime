import math

class ClockLogic:

    @staticmethod
    def get_angles(hour, minute, second):
        second_angle = math.radians(second * 6 - 90)
        minute_angle = math.radians(minute * 6 + second * 0.1 - 90)
        hour_angle = math.radians((hour % 12) * 30 + minute * 0.5 - 90)

        return hour_angle, minute_angle, second_angle