class Clock:
    def __init__(self):
        self.progress = 95

    def tick(self):
        self.progress = (self.progress + 1) % 100

    def get_progress_str(self):
        return str(self.progress)
