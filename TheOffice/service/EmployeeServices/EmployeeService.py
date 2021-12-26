import pygame


class EmployeeService:
    def __init__(self, room_board, hustle_thread, consumer_thread):
        self.employee_list = []
        self.init_extras()
        self.room_board = room_board
        self.init_threads(hustle_thread, consumer_thread)

    def init_threads(self, hustle_thread, consumer_thread):
        self.hustle_thread = hustle_thread
        self.consumer_thread = consumer_thread

    def init_extras(self):
        self.dragged_emp_i = -1

    def add_employee(self, emp):
        self.employee_list.append(emp)

    def drag_emp_if_selected(self):
        if self.dragged_emp_i != -1:
            self.employee_list[self.dragged_emp_i].rect.x = pygame.mouse.get_pos()[0]
            self.employee_list[self.dragged_emp_i].rect.y = pygame.mouse.get_pos()[1]

    def pick_up_employee(self, index):
        if self.employee_list[index].rect.collidepoint(pygame.mouse.get_pos()):
            self.dragged_emp_i = index
            self.handle_emp_desk_detach_event(self.employee_list[self.dragged_emp_i])

    def put_down_employee(self, index):
        print(index)
        print(self.employee_list[index].rect)
        if self.employee_list[index].rect.collidepoint(pygame.mouse.get_pos()):
            self.handle_emp_desk_collide_event(self.employee_list[self.dragged_emp_i])
        self.dragged_emp_i = -1

    def handle_emp_desk_detach_event(self, emp):
        if emp.desk_observer != None:
            emp.desk_observer.taken = False
            emp.detach_desk()
            try:
                self.hustle_thread.pop_emp(emp)
            except:
                self.consumer_thread.pop_emp(emp)

    def handle_emp_desk_collide_event(self, emp):
        for floor_i in range(0, len(self.room_board)):
            room_list = list(self.room_board[floor_i].values())
            for room_i in range(0, len(self.room_board[floor_i])):
                for desk_i in range(0, 4):
                    # print(type(room_list[room_i]).__name__)
                    # print("table rect ", room_list[room_i].action_objects[desk_i].rect)
                    # print("emp rect" ,emp.rect)
                    # print("dolided?",emp.rect.colliderect(room_list[room_i].action_objects[desk_i].rect))
                    if emp.rect.colliderect(room_list[room_i].action_objects[desk_i].rect):
                        # print("Collision detected with:", emp.name)
                        print("czy taken?",self.action_object_taken(room_list, room_i, desk_i ))
                        if self.action_object_taken(room_list, room_i, desk_i ) == False:
                            if type(room_list[room_i]).__name__ == "DiningRoom":
                                self.consumer_thread.insert_emp(emp)
                                print(self.consumer_thread.emp_dict)
                            elif type(room_list[room_i]).__name__ == "OfficeRoom":
                                self.hustle_thread.insert_emp(emp)
                            if self.consumer_thread.get_emp(id(emp)) != None:
                                self.consumer_thread.pop_emp(emp)
                            self.adjust_emp_to_desk(emp, room_list[room_i].action_objects[desk_i])
                            self.update_rooms_desk_status(room_list, room_i, desk_i, True)
                            emp.attach_desk(room_list[room_i].action_objects[desk_i])


    def adjust_emp_to_desk(self, emp, desk):
        emp.rect.y = desk.rect.y - 20

    def action_object_taken(self, room_list, room_i, desk_i):
        action_object = room_list[room_i].action_objects[desk_i]
        # print(type(action_object.taken).__name__)
        # print("tru czynie tru",(action_object.taken == True and action_object.taken == True))
        if type(action_object.taken).__name__ != "list":
            return action_object.taken
        return (action_object.taken[0] == True and action_object.taken[1] == True)

    def update_rooms_desk_status(self, room_list, room_i, desk_i, status):
        room_list[room_i].action_objects[desk_i].taken = status
