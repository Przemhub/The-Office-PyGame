class EmpDeskEvent:
    def __init__(self, room_board, hustle_thread, consumer_thread):
        self.room_board = room_board
        self.hustle_thread = hustle_thread
        self.consumer_thread = consumer_thread

    def handle_detach_event(self,emp):
        if emp._data.desk_observer != None:
            emp._data.desk_observer.taken = False
            emp._data.detach_desk()
            self.hustle_thread.pop_emp(emp)

    def handle_collide_event(self,emp):
        # print(self.room_board[0][0].action_objects[0].rect.x)
        # print(self.room_board[0][0].action_objects[0].rect.y)
        for floor in range(0, len(self.room_board)):
            for room_i in range(0, len(self.room_board[floor])):
                for desk_i in range(0, 4):
                    if emp.rect.colliderect(self.room_board[floor][room_i].action_objects[desk_i].rect):
                        # print("Collision detected with:", emp._data.name)
                        if self.desk_taken(floor, room_i, desk_i,) == False:
                            self.hustle_thread.insert_emp(emp)
                            if self.consumer_thread.get_emp(id(emp)) != None:
                                self.consumer_thread.pop_emp(emp)
                            self.adjust_emp_to_desk(emp, self.room_board[floor][room_i].action_objects[desk_i])
                            self.update_rooms_desk_status(floor, room_i, desk_i, True)
                            emp._data.attach_desk(self.room_board[floor][room_i].action_objects[desk_i]._data)


    def adjust_emp_to_desk(self, emp, desk):
        emp.rect.y = desk.rect.y - 10

    def desk_taken(self, floor, room_i, desk_i):
        return self.room_board[floor][room_i]._data.desks[desk_i].taken

    def update_rooms_desk_status(self, floor, room_i, desk_i, status):
        self.room_board[floor][room_i]._data.desks[desk_i].taken = status