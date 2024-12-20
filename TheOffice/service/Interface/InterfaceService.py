Reimport pygame
from pygame import image
from pygame.rect import Rect

from model.Interface.ClockElement import ClockElement
from model.Interface.InterfaceElement import InterfaceElement
from model.Time.CalendarElement import CalendarElement
from service.Interface.RoomPurchaseService import RoomPurchaseService


class InterfaceService:
    def __init__(self):
        self.time_dist = 1800
        self.timestamp = pygame.time.get_ticks()
        self.room_purchase_service = RoomPurchaseService()

        self.calendar_element = CalendarElement()
        self.clock_element = ClockElement()
        self.arrow_right_element = InterfaceElement(Rect(100, 100, 100, 100), image.load("../resources/interface/icons/accept.png"),
                                                    self.switch_view_right)
        self.arrow_left_element = InterfaceElement(Rect(100, 100, 100, 100), image.load("../resources/interface/icons/accept.png"),
                                                   self.switch_view_left)
        self.accept_element = InterfaceElement(Rect(300, 400, 100, 100), image.load("../resources/interface/icons/accept.png"),
                                               self.click_accept)
        self.reject_element = InterfaceElement(Rect(400, 400, 100, 100), image.load("../resources/interface/icons/reject.png"),
                                               self.click_reject)
        self.calendar_icon = InterfaceElement(Rect(220, 8, 75, 60), image.load("../resources/interface/icons/calendar.png"),
                                              self.click_calendar)
        self.element_list = [self.arrow_left_element, self.arrow_right_element, self.accept_element, self.reject_element, self.clock_element]

        self.view_element = InterfaceElement(Rect(300, 400, 100, 100), image.load("../resources/interface/icons/accept.png"))
        self.view_type = 1
        self.PURCHASE_ROOM = 1
        self.HIRE_EMPLOYEE = 2
        self.SETTINGS = 3
        self.CALENDAR = 4

    def update_time(self):
        if pygame.time.get_ticks() - self.timestamp > self.time_dist:
            self.clock_element.tick()
            theta = 360 * self.clock_element.progress / 100
            self.clock_element.update_clock(theta)
            if self.clock_element.progress == 99:
                self.calendar_element.update()
            self.timestamp = pygame.time.get_ticks()

    def get_clock_progress_str(self):
        return self.clock_element.get_progress_str()

    def switch_view_right(self):
        if self.view_type == self.PURCHASE_ROOM:
            self.room_purchase_service.next_room()

    def switch_view_left(self):
        if self.view_type == self.PURCHASE_ROOM:
            self.room_purchase_service.previous_room()

    def click_accept(self):
        self.view_element.rect = self.view_element.rect.move(50, 0)

    def click_reject(self):
        self.view_element.rect = self.view_element.rect.move(-50, 0)

    def click_calendar(self):
        self.view_type = self.CALENDAR
