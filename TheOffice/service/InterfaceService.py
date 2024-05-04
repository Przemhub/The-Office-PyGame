from model.Interface.Toolbar import Toolbar


class InterfaceService:
    def __init__(self, toolbar: Toolbar):
        self.LEFT_WING = 0
        self.RIGHT_WING = 1
        self.left_down = False
        self.right_down = False
        self.toolbar = toolbar

    def pull_down_animation(self):
        if self.left_down:
            if self.is_not_fully_down(self.toolbar.left_wing):
                self.toolbar.left_wing = self.move_wing(self.toolbar.left_wing)
        elif self.right_down:
            if self.is_not_fully_down(self.toolbar.right_wing):
                self.toolbar.right_wing = self.move_wing(self.toolbar.right_wing)

    def move_wing(self, wing):
        if wing.top < self.toolbar.rect.bottom - 50:
            return wing.move(0, 35)
        elif wing.top < self.toolbar.rect.bottom - 20:
            return wing.move(0, 15)
        return wing.move(0, 5)

    def pull_down_wing(self, side):
        if side == self.LEFT_WING:
            self.left_down = True
        else:
            self.right_down = True

    def is_not_fully_down(self, wing):
        return wing.top < self.toolbar.rect.bottom