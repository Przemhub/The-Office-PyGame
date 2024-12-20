import pygame
from pygame import image, time
from pygame.rect import Rect

from model.Interface.ClockElement import ClockElement
from model.Interface.StaticElement import StaticElement
from model.Interface.InterfaceElement import InterfaceElement
from model.Interface.CalendarElement import CalendarElement
from service.Interface.RoomPurchaseService import RoomPurchaseService


class InterfaceService:
    def __init__(self):
        self.time_dist = 1800
        self.timestamp = time.get_ticks()
        self.room_purchase_service = RoomPurchaseService()

        self.calendar_element = CalendarElement(Rect(260, 170, 283, 192), image.load("../resources/interface/elements/calendar/calendar.png"))
        self.clock_element = ClockElement(Rect(20, 0, 1, 45), image.load("../resources/interface/elements/clock.png"))
        self.arrow_right_element = InterfaceElement(Rect(570, 170, 100, 170), image.load("../resources/interface/elements/right.png"),
                                                    self.switch_view_right)
        self.arrow_left_element = InterfaceElement(Rect(120, 170, 100, 170), image.load("../resources/interface/elements/left.png"),
                                                   self.switch_view_left)
        self.accept_element = InterfaceElement(Rect(300, 400, 90, 90), image.load("../resources/interface/icons/accept.png"),
                                               self.click_accept)
        self.reject_element = InterfaceElement(Rect(420, 400, 80, 80), image.load("../resources/interface/icons/reject.png"),
                                               self.click_reject)
        self.calendar_icon = StaticElement(Rect(220, 8, 75, 60), image.load("../resources/interface/icons/calendar.png"),
                                           self.click_calendar)
        self.element_list = [self.arrow_left_element, self.arrow_right_element, self.accept_element, self.reject_element,
                             self.clock_element, self.calendar_icon]

        self.view_element = InterfaceElement(Rect(300, 400, 100, 100), image.load("../resources/interface/icons/accept.png"))

        self.NO_TYPE = 0
        self.PURCHASE_ROOM = 1
        self.HIRE_EMPLOYEE = 2
        self.SETTINGS = 3
        self.CALENDAR = 4
        self.view_type = self.NO_TYPE

    def update_time(self):
        if time.get_ticks() - self.timestamp > self.time_dist:
            self.clock_element.tick()
            theta = 360 * self.clock_element.progress / 100
            self.clock_element.update_clock(theta)
            if self.clock_element.progress == 99:
                self.calendar_element.update()
            self.timestamp = time.get_ticks()

    def get_clock_progress_str(self):
        return self.clock_element.get_progress_str()

    # on clicks

    def switch_view_right(self):
        if self.view_type == self.PURCHASE_ROOM:
            self.room_purchase_service.next_room()

    def switch_view_left(self):
        if self.view_type == self.PURCHASE_ROOM:
            self.room_purchase_service.previous_room()

    def click_accept(self):
        self.view_type = self.NO_TYPE

    def click_reject(self):
        self.view_type = self.NO_TYPE

    def click_calendar(self):
        if self.view_type == self.CALENDAR:
            self.view_type = self.NO_TYPE
        else:
            self.view_type = self.CALENDAR

    # on hovers

    def drop_shadow(self, element : InterfaceElement):
        element.is_hover = True
