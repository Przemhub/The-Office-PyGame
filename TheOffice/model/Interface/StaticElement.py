from model.Interface.InterfaceElement import InterfaceElement


# Element that never disappears
class StaticElement(InterfaceElement):
    def __init__(self, rect, image, on_click=None, on_hover=None):
        super().__init__(rect, image, on_click)
