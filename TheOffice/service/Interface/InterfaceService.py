import datetime

import pygame

from model.Interface.Toolbar import Toolbar
from model.Interface.Wing import Wing
from model.Time.Calendar import Calendar
from model.Time.Clock import Clock


class InterfaceService:
    def __init__(self):
        self.LEFT_WING = 0
        self.RIGHT_WING = 1
        self.left_down = False
        self.right_down = False
        self.time_dist = 1800
        self.timestamp = pygame.time.get_ticks()
        self.calendar = Calendar()
        self.toolbar = Toolbar()
        self.clock = Clock()

    def pull_down_animation(self):
        if self.left_down:
            if self.is_not_fully_down(self.toolbar.left_wing):
                self.move_wing_down(self.toolbar.left_wing)
        elif self.right_down:
            if self.is_not_fully_down(self.toolbar.right_wing):
                self.move_wing_down(self.toolbar.right_wing)
        else:
            if self.is_not_fully_up(self.toolbar.left_wing):
                self.move_wing_up(self.toolbar.left_wing)

    def move_wing_down(self, wing: Wing):
        if wing.rect.top < self.toolbar.rect.bottom - 50:
            wing.gadget.move(0, 35)  # move the gadget inside the wing with it
            wing.move(0, 35)
        elif wing.rect.top < self.toolbar.rect.bottom - 20:
            wing.gadget.move(0, 15)
            wing.move(0, 15)
        wing.gadget.move(0, 5)
        wing.move(0, 5)

    def pull_push_wing(self, side):
        if side == self.LEFT_WING:
            self.left_down = not self.left_down
        else:
            self.right_down = True

    def move_wing_up(self, wing):
        if wing.rect.top > self.toolbar.rect.bottom - 50:
            wing.gadget.move(0, -20)
            wing.move(0, -20)
        wing.move(0, -50)
        wing.gadget.move(0, -50)

    def is_not_fully_down(self, wing):
        return wing.rect.top < self.toolbar.rect.bottom

    def is_not_fully_up(self, wing):
        return wing.rect.bottom > self.toolbar.rect.top

    def update_time(self):
        if pygame.time.get_ticks() - self.timestamp > self.time_dist:
            self.clock.tick()
            theta = 360 * self.clock.progress / 100
            self.toolbar.update_clock(theta)
            if self.clock.progress == 99:
                self.calendar.update()

            self.timestamp = pygame.time.get_ticks()

    def get_clock_progress_str(self):
        return self.clock.get_progress_str()
