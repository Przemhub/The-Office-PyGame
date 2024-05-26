import datetime
import math

import pygame

from model.Interface.Toolbar import Toolbar
from model.Time.Calendar import Calendar
from model.Time.Clock import Clock


class TimeService:
    def __init__(self, toolbar: Toolbar):
        self.timestamp = pygame.time.get_ticks()
        self.clock = Clock()
        self.time_dist = 1800
        self.toolbar = toolbar
        self.calendar_matrix = self.init_calendar_matrix(2000)
        # day 0 means 1st january
        # we are counting only work days, so a month has 20 days
        # a year has 240 days
        self.current_day = 0

    def update_time(self):
        if pygame.time.get_ticks() - self.timestamp > self.time_dist:
            self.clock.tick()
            theta = 360 * self.clock.progress / 100
            self.toolbar.update_clock(theta)
            if self.clock.progress == 100:
                self.current_day += 1
            self.timestamp = pygame.time.get_ticks()

    def get_progress_str(self):
        return self.clock.get_progress_str()

    def init_calendar_matrix(self, year):
        calendar_matrix = []
        date = datetime.date(year, 1, 1)
        DAYS_PER_PAGE = 35
        # set a matrix where row is month and column is a day of month
        for days in range(0, 365):
            day = (date + datetime.timedelta(days)).day
            page = math.floor(days / DAYS_PER_PAGE)
            if days % DAYS_PER_PAGE == 0:
                calendar_matrix.append([])
            calendar_matrix[page].append(day)
        return calendar_matrix
