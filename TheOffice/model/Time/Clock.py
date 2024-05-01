import pygame.time


class Clock:
    def __init__(self):
        self.timestamp = pygame.time.get_ticks()
        self.progress = 0
        self.time_dist = 1800

    def tick(self):
        if pygame.time.get_ticks() - self.timestamp > self.time_dist:
            self.progress = (self.progress + 1) % 101
            self.timestamp = pygame.time.get_ticks()

    def get_progress_str(self):
        return str(self.progress)
