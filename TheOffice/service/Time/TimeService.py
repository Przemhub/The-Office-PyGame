import pygame

from model.Interface.Toolbar import Toolbar
from model.Time.Calendar import Calendar
from model.Time.Clock import Clock


class TimeService:
    def __init__(self, toolbar: Toolbar):
        self.timestamp = pygame.time.get_ticks()
        self.clock = Clock()
        self.time_dist = 1800
        self.calendar = Calendar()
        self.toolbar = toolbar

    def update_time(self):
        if pygame.time.get_ticks() - self.timestamp > self.time_dist:
            self.clock.tick()
            theta = 360 * self.clock.progress/100
            self.toolbar.update_clock(theta)
            if self.clock.progress == 100:
                self.calendar.update_calendar()
            self.timestamp = pygame.time.get_ticks()

    def get_progress_str(self):
        return self.clock.get_progress_str()
