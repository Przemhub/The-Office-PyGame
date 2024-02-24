from pygame import sprite


class Room(sprite.Sprite):
    def __init__(self, neighbour_rooms):
        sprite.Sprite.__init__(self)
        self.neighbour_rooms = neighbour_rooms
        self.action_objects = []

    def is_free(self):
        for action_obj in self.action_objects:
            if not action_obj.taken:
                return True
        return False

    def get_base_coordinates(self):
        x = 0
        y = 230
        # make x and y indifferent to the position of camera
        if len(self.neighbour_rooms) is not 0:
            x = self.get_first_room().rect.x
            y = self.get_first_room().rect.y

        for room in self.neighbour_rooms:
            x += room.image.get_width()
        return x, y

    def get_first_room(self):
        return self.neighbour_rooms[0]
