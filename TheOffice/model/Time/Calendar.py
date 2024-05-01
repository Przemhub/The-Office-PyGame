class Calendar:
    def __init__(self):
        # day 0 means 1st january
        # we are counting only work days, so a month has 20 days
        # a year has 240 days
        self.day = 0


    def update_calendar(self):
        self.day += 1