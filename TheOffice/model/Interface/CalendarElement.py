import datetime
from os import listdir

import pygame.image
from pygame import font, Rect

from model.Interface.InterfaceElement import InterfaceElement


class CalendarElement(InterfaceElement):
    def __init__(self, rect, image):
        super().__init__(rect, image)
        self.font = font.SysFont("Calibri", 25, True)
        self.page_images = [pygame.transform.scale(pygame.image.load("../resources/interface/elements/calendar/pages/" + page), (253, 193))
                            for page in listdir("../resources/interface/elements/calendar/pages")]
        self.page_rect = Rect(270, 160, self.page_images[0].get_width(), self.page_images[0].get_height())
        self.current_page = 0
        self.current_date = datetime.date(2024, 1, 1)
        self.init_texts()
        self.page_marker_pos = [1, 0, 0]
        self.page_marker_rect_fixed_pos = (272, 176)
        self.marker_width = 37
        self.marker_height = 36
        self.page_marker_rect = Rect(280 + self.page_marker_pos[0] * 31, 176 + self.page_marker_pos[1] * 35, self.marker_width,
                                     self.marker_height)
        self._marker_offset_dict = {0: 4, 1: 5, 2: 0, 3: 3, 4: 6, 5: 0, 6: 4, 7: 0, 8: 2, 9: 5, 10: 0, 11: 1}

    def update(self):
        self.current_date += datetime.timedelta(1)
        # if next month starts
        if self.current_date.day == 1:
            self.page_marker_pos = [self.get_marker_offset(), 0, self.page_marker_pos[2] + 1]
        # if next week starts
        elif self.page_marker_pos[0] == 6:
            self.page_marker_pos = [0, self.page_marker_pos[1] + 1, self.page_marker_pos[2]]
        else:
            self.page_marker_pos[0] += 1
        self.page_marker_rect.x = self.page_marker_rect_fixed_pos[0] + self.page_marker_pos[0] * self.marker_width
        self.page_marker_rect.y = self.page_marker_rect_fixed_pos[1] + self.page_marker_pos[1] * self.marker_height

    def move(self, x, y):
        self.rect = self.rect.move(x, y)
        self.page_rect = self.page_rect.move(x, y)
        self.page_marker_rect = self.page_marker_rect.move(x, y)
        self.page_marker_rect_fixed_pos = (self.page_marker_rect_fixed_pos[0] + x, self.page_marker_rect_fixed_pos[1] + y)

    def get_marker_offset(self):
        return self._marker_offset_dict.get(self.current_page)

    def init_texts(self):
        font = pygame.font.SysFont("Calibri", 30, True)
        self.month_text_rect = pygame.Rect(260, 140, 100, 24)
        text_january = font.render("January", True, 0)
        text_february = font.render("February", True, 0)
        text_march = font.render("March", True, 0)
        text_april = font.render("April", True, 0)
        text_may = font.render("May", True, 0)
        text_june = font.render("June", True, 0)
        text_july = font.render("July", True, 0)
        text_august = font.render("August", True, 0)
        text_september = font.render("September", True, 0)
        text_october = font.render("October", True, 0)
        text_november = font.render("November", True, 0)
        text_december = font.render("December", True, 0)
        self._month_text_dict = {0: text_january, 1: text_february, 2: text_march, 3: text_april, 4: text_may,
                                 5: text_june, 6: text_july, 7: text_august, 8: text_october, 9: text_september,
                                 10: text_november, 11: text_december}

    def get_month_text(self):
        return self._month_text_dict.get(self.current_page)
