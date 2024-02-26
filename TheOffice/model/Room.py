from pygame import sprite


class Room(sprite.Sprite):
    def __init__(self, board_pos, room_board):
        sprite.Sprite.__init__(self)
        # Where the room needs to be placed
        self.place_index = board_pos[0]
        self.floor = board_pos[1]
        self.room_board = room_board
        self.action_objects = []
        #               (width, height)
        self.room_size = (360, 360)

    def is_free(self):
        for action_obj in self.action_objects:
            if not action_obj.taken:
                return True
        return False

    def get_base_coordinates(self):
        x = 0
        y = 230
        # make x and y indifferent to the position of camera
        if len(self.room_board[self.floor]) > 0:
            x = self.get_first_room().rect.x
            y = self.get_first_room().rect.y
        x += self.place_index * self.room_size[0]

        # if we are building a new floor, then we want to align coordinates with the previous floor room
        if self.floor > 0:
            y = self.room_board[self.floor - 1][self.place_index].rect.y - self.room_size[1]
            x = self.room_board[self.floor - 1][self.place_index].rect.x

        return x, y

    def get_first_room(self):
        return self.room_board[self.floor][0]
