import pygame

from model.Time.Calendar import Calendar
from model.Time.Clock import Clock


class TimeService:
    def __init__(self):
        self.timestamp = pygame.time.get_ticks()
        self.clock = Clock()
        self.time_dist = 1800
        self.calendar = Calendar()

    def update_time(self):
        if pygame.time.get_ticks() - self.timestamp > self.time_dist:
            self.clock.tick()
            if self.clock.progress == 100:
                self.calendar.update_calendar()
            self.timestamp = pygame.time.get_ticks()

    def get_progress_str(self):
        return self.clock.get_progress_str()
