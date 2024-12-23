import datetime
from os import listdir

import pygame.image
from pygame import font, Rect, Surface

from model.Interface.InterfaceElement import InterfaceElement


class CalendarElement(InterfaceElement):
    def __init__(self, rect, image):
        super().__init__(rect, image)
        self.font = font.SysFont("Calibri", 25, True)
        self._page_images = [pygame.transform.scale(pygame.image.load("../resources/interface/elements/calendar/pages/" + page), (253, 193))
                             for page in listdir("../resources/interface/elements/calendar/pages")]
        self.page_rect = Rect(270, 160, self._page_images[0].get_width(), self._page_images[0].get_height())
        self._current_page = 0
        self.current_date = datetime.date(2024, 1, 1)
        self.init_texts()
        self.page_marker_pos = [1, 0, 0]
        self.page_marker_rect_fixed_pos = (263, 176)
        self.marker_width = 37
        self.marker_height = 36
        self.page_marker_rect = Rect(265 + self.page_marker_pos[0] * 31, 176 + self.page_marker_pos[1] * 35, self.marker_width,
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

    def get_current_page_image(self):
        return self._page_images[self._current_page]

    def get_marker_offset(self):
        return self._marker_offset_dict.get(self._current_page)

    def init_texts(self):
        sysfont = font.SysFont("Calibri", 30, True)
        self.month_text_rect = Rect(260, 140, 100, 24)
        self.text_background = Surface((self.month_text_rect.width + 45, self.month_text_rect.height + 10))
        self.text_background.set_alpha(200)
        self.text_background.fill((255, 255, 255))
        self._month_text_dict = {0: sysfont.render("January", True, 0), 1: sysfont.render("February", True, 0),
                                 2: sysfont.render("March", True, 0),
                                 3: sysfont.render("April", True, 0), 4: sysfont.render("May", True, 0),
                                 5: sysfont.render("June", True, 0), 6: sysfont.render("July", True, 0),
                                 7: sysfont.render("August", True, 0),
                                 8: sysfont.render("September", True, 0), 9: sysfont.render("October", True, 0),
                                 10: sysfont.render("November", True, 0), 11: sysfont.render("December", True, 0)}

    def get_month_text(self):
        return self._month_text_dict.get(self._current_page)

    def next_page(self):
        self._current_page += 1
        if self._current_page == 12:
            self._current_page = 0

    def previous_page(self):
        self._current_page -= 1
        if self._current_page < 0:
            self._current_page = 11

    def at_current_page(self):
        return self._current_page == self.page_marker_pos[2]

    def is_payday(self):
        return self.current_date.day == 10

    def is_day_after_payday(self):
        return self.current_date.day == 11
