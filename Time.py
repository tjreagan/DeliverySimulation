# Thomas Reagan
# ID: 001265074

import datetime

# Class for a timer object for the trucks being used
class Time:
    # Constructor initializes the clock to 8:00AM
    def __init__(self):
        self.total_seconds = 28800
        self.time = datetime.timedelta(0, self.total_seconds)

    # Function to increment the timer based on distance between deliveries
    def add_time(self, distance):
        time_to_add = distance / 0.005
        self.total_seconds += time_to_add
        self.time = datetime.timedelta(0, self.total_seconds)