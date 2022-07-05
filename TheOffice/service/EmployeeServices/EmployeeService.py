import pygame

from model.Employee.Employee import Employee
from service.EmployeeServices.ConsumeService import ConsumeService
from service.EmployeeServices.NeedsService import NeedsService
from service.EmployeeServices.WorkingService import WorkingService


class EmployeeService:
    def __init__(self, room_board):
        self.employee_list = []
        self.init_extras()
        self.room_board = room_board
        self.init_threads()

    def init_threads(self):
        self.working_service_conc = WorkingService()
        self.consumer_service_conc = ConsumeService()
        self.needs_service_conc = NeedsService()
        self.working_service_conc.start()
        self.needs_service_conc.start()
        self.consumer_service_conc.start()

    def create_employee(self, x, y, name, company):
        emp = Employee(x, y, name, company)
        self.employee_list.append(emp)
        self.needs_service_conc.insert_emp(emp)

    def init_extras(self):
        self.dragged_emp_i = -1
        self.previous_time = pygame.time.get_ticks()
        self.wait_time = 0.1 * 1000

    def drag_emp_if_selected(self):
        if self.dragged_emp_i != -1:
            self.employee_list[self.dragged_emp_i].rect.centerx = pygame.mouse.get_pos()[0]
            self.employee_list[self.dragged_emp_i].rect.centery = pygame.mouse.get_pos()[1]

    def pick_up_employee(self, index):
        if self.employee_list[index].rect.collidepoint(pygame.mouse.get_pos()):
            self.dragged_emp_i = index
            self.handle_emp_desk_detach_event(self.employee_list[self.dragged_emp_i])

    def put_down_employee(self, index):
        # print(index)
        # print(self.employee_list[index].rect)
        if self.employee_list[index].rect.collidepoint(pygame.mouse.get_pos()):
            self.handle_emp_desk_collide(self.employee_list[self.dragged_emp_i])
        self.dragged_emp_i = -1

    def handle_emp_desk_detach_event(self, emp):
        if emp.desk_observer != None:
            emp.desk_observer.taken = False
            emp.remove_from_desk()
            try:
                self.working_service_conc.pop_emp(emp)
            except:
                self.consumer_service_conc.pop_emp(emp)

    def handle_emp_desk_collide(self, emp):
        for floor_i in range(0, len(self.room_board)):
            room_list = list(self.room_board[floor_i].values())
            for room_i in range(0, len(self.room_board[floor_i])):
                for desk_i in range(0, len(room_list[room_i].action_objects)):
                    # print(type(room_list[room_i]).__name__)
                    # print("table rect ", room_list[room_i].action_objects[desk_i].rect)
                    # print("emp rect" ,emp.rect)
                    # print("dolided?",emp.rect.colliderect(room_list[room_i].action_objects[desk_i].rect))
                    if emp.rect.colliderect(room_list[room_i].action_objects[desk_i].rect):
                        # print("Collision detected with:", emp.name)
                        # print("czy taken?", self.action_object_taken(room_list, room_i, desk_i))
                        if self.action_object_taken(room_list, room_i, desk_i) == False:
                            if type(room_list[room_i]).__name__ == "DiningRoom":
                                self.consumer_service_conc.insert_emp(emp)
                                # print(self.consumer_thread.emp_dict)
                            elif type(room_list[room_i]).__name__ == "OfficeRoom":
                                self.working_service_conc.insert_emp(emp)
                            self.update_action_object_status(room_list[room_i].action_objects[desk_i])
                            self.adjust_emp_to_action_object(emp, room_list[room_i].action_objects[desk_i],
                                                             room_list[room_i], desk_i)
                            emp.set_desk(room_list[room_i].action_objects[desk_i])

    def adjust_emp_to_action_object(self, emp, desk, room, desk_i):
        print(desk_i)
        if type(room).__name__ == "DiningRoom":
            # print(desk_i)
            emp.rect.x = desk.rect.x
            emp.rect.y = desk.rect.y
            if desk_i % 2 != 0:
                emp.sitting_sprite_right()
                emp.rect = emp.rect.move(-20, - 27)
            else:
                emp.sitting_sprite_left()
                emp.rect = emp.rect.move(0, - 30)


        elif type(room).__name__ == "OfficeRoom":
            emp.rect.x = desk.rect.x
            emp.rect.y = desk.rect.y
            emp.rect = emp.rect.move(10, - 10)
            emp.sitting_sprite_back()

    def check_every_employee(self):
        for emp in self.employee_list:
            self.check_needs_and_move(emp)

    def check_needs_and_move(self, emp):
        # only use it once when the needs are below threshold
        if emp.destination is None:
            if emp.is_hungry():
                if emp.is_sitting_down():
                    emp.remove_from_desk()
                    #available room searching algorithm
                for floor_i in range(0, len(self.room_board)):
                    room_list = list(self.room_board[floor_i].values())
                    for room_i in range(0, len(self.room_board[floor_i])):
                        if emp.rect.colliderect(room_list[room_i].rect):
                            room_dist = 1
                            while True:
                                if room_i + room_dist < len(room_list):
                                    if type(room_list[room_i + room_dist]).__name__ == "DiningRoom":
                                        emp.destination = room_list[room_i + room_dist]
                                        break
                                if room_i - room_dist >= 0:
                                    if type(room_list[room_i - room_dist]).__name__ == "DiningRoom":
                                        emp.destination = room_list[room_i - room_dist]
                                        break
                                if room_i - room_dist < 0 and room_i + room_dist >= len(room_list):
                                    break
                                room_dist += 1
        else:
            if self.move_to_destination_check_if_arrived(emp):
                self.change_destination(emp)
    
    def change_destination(self, emp):
        if emp.destination.__class__.__base__.__name__ == "Room":
            for action_object in emp.destination.action_objects:
                if not self.action_object_taken_by_object(action_object):
                    emp.destination = action_object
                    print(action_object.rect)
                    break
        elif emp.destination.__class__.__base__.__name__ == "ActionObject":
            emp.rect = emp.rect.move(5, 0)
            self.consumer_service_conc.insert_emp(emp)
            self.update_action_object_status(emp.destination)
            self.adjust_emp_to_action_object(emp, emp.destination, emp.destination.room,
                                             emp.destination.room.action_objects.index(emp.destination))
            emp.set_desk(emp.destination)
            emp.destination = None

    def move_to_destination_check_if_arrived(self, emp):
        x = 0
        y = 0
        direction = ''
        if emp.destination.rect.x > emp.rect.x + 5:
            x = 5
            direction = 'R'
        elif emp.destination.rect.x < emp.rect.x - 5:
            x = -5
            direction = 'L'
        else:
            return True

        emp.rect = emp.rect.move(x, y)
        self.animate_employee(direction)
        return False

    def action_object_taken(self, room_list, room_i, desk_i):
        action_object = room_list[room_i].action_objects[desk_i]
        # print(type(action_object.taken).__name__)
        # print("tru czynie tru",(action_object.taken == True and action_object.taken == True))
        return action_object.taken

    def action_object_taken_by_object(self, action_object):
        return action_object.taken

    def update_action_object_status(self, action_object):
        action_object.taken = True

    def animate_employee(self, direction):

        if  pygame.time.get_ticks() - self.previous_time > self.wait_time:
            self.previous_time = pygame.time.get_ticks()
            for employee in self.employee_list:
                if direction == 'L':
                    if employee.current_position == employee.WALK_LEFT:
                        employee.change_walking_sprite(employee.WALK_LEFT2)
                    elif employee.current_position == employee.WALK_LEFT2:
                        employee.change_walking_sprite(employee.WALK_LEFT3)
                    elif employee.current_position == employee.WALK_LEFT3:
                        employee.change_walking_sprite(employee.WALK_LEFT4)
                    else:
                        employee.change_walking_sprite(employee.WALK_LEFT)
                elif direction == 'R':
                    if employee.current_position == employee.WALK_RIGHT:
                        employee.change_walking_sprite(employee.WALK_RIGHT2)
                    elif employee.current_position == employee.WALK_RIGHT2:
                        employee.change_walking_sprite(employee.WALK_RIGHT3)
                    elif employee.current_position == employee.WALK_RIGHT3:
                        employee.change_walking_sprite(employee.WALK_RIGHT4)
                    else:
                        employee.change_walking_sprite(employee.WALK_RIGHT)
                    print(employee.current_position)