class RoomPurchaseService:
    def __init__(self):
        self.room_list = []
        self.room_index = 0

    def next_room(self):
        self.room_index += 1
        self.room_index %= len(self.room_list)

    def previous_room(self):
        self.room_index -= 1
        if self.room_index < 0:
            self.room_index = 0

