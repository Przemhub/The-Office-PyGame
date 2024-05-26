from pygame import image, font, Rect

from model.Interface.Gadget import Gadget


class Calendar(Gadget):
    def __init__(self):
        super().__init__(Rect(40,-222,283,192), image.load("../resources/interface/dropdowns/calendar.png"))
        self.font = font.SysFont("Calibri", 7, True)
        self.calendar_text = self.font.render("Paper sold: ", True, (255, 255, 255))
