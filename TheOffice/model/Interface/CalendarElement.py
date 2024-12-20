import datetime
import math
from os import listdir

import pygame.image
from pygame import image, font, Rect

from model.Interface.InterfaceElement import InterfaceElement


class CalendarElement(InterfaceElement):
    def __init__(self, rect, image):
        super().__init__(rect, image)
        self.font = font.SysFont("Calibri", 25, True)
        self.page_images = [pygame.transform.scale(pygame.image.load("../resources/interface/elements/calendar/pages/" + page), (253, 193))
                            for page in listdir("../resources/interface/elements/calendar/pages")]
        self.page_rect = Rect(270, 160, self.page_images[0].get_width(), self.page_images[0].get_height())
        self.current_page = 0
        self.calendar_matrix = self.init_calendar_matrix(2024)
        self.current_date = datetime.date(2024, 1, 1)
        offset = datetime.date(2024, self.current_date.month, 1).weekday()
        self.page_marker_pos = [1, 0]
        self.page_marker_rect_fixed_pos = (278, 176)
        self.page_marker_rect = Rect(278 + self.page_marker_pos[0] * 32, 176 + self.page_marker_pos[1] * 35, 34, 36)

    def init_calendar_matrix(self, year):
        calendar_matrix = [[]]
        date = datetime.date(year, 1, 1)
        DAYS_PER_PAGE = 35
        # first page starts with 31 of december from last year
        calendar_matrix[0].append(31)
        # set a matrix where row is month and column is a day of month
        for days in range(0, 365):
            day = (date + datetime.timedelta(days)).day
            page = math.floor(days / DAYS_PER_PAGE)
            if days % DAYS_PER_PAGE == 0:
                calendar_matrix.append([])
            calendar_matrix[page].append(day)
        return calendar_matrix

    def update(self):
        self.current_date += datetime.timedelta(1)
        # if next month starts
        if self.current_date.day == 1:
            offset = datetime.date(2024, self.current_date.month, 1).weekday()
            self.page_marker_pos = [0 + offset, 0]
        # if next week starts
        elif self.page_marker_pos[0] == 7:
            self.page_marker_pos = [0, self.page_marker_pos[1] + 1]
        else:
            self.page_marker_pos[0] += 1
        self.page_marker_rect.x = self.page_marker_rect_fixed_pos[0] + self.page_marker_pos[0] * 32
        self.page_marker_rect.y = self.page_marker_rect_fixed_pos[1] + self.page_marker_pos[1] * 35

    def move(self, x, y):
        self.rect = self.rect.move(x, y)
        self.page_rect = self.page_rect.move(x, y)
        self.page_marker_rect = self.page_marker_rect.move(x, y)
        self.page_marker_rect_fixed_pos = (self.page_marker_rect_fixed_pos[0] + x, self.page_marker_rect_fixed_pos[1] + y)
