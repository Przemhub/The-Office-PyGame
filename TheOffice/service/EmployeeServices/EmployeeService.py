from pygame import time, mouse
from model.Employee.Employee import Employee
from model.Ground import Ground
from service.EmployeeServices.ConsumeService import ConsumeService
from service.EmployeeServices.NeedsService import NeedsService
from service.EmployeeServices.TaskService import TaskService
from service.EmployeeThreads.EmployeeNeedThread import EmployeeNeedThread
from service.EmployeeThreads.EmployeeTaskThread import EmployeeTaskThread


class EmployeeService:
    def __init__(self, room_board, ground: Ground):
        self.employee_list = []
        self.init_extras()
        self.room_board = room_board
        self.ground = ground
        self.initial_ticks = time.get_ticks()
        self.init_threads()

    def init_threads(self):
        self.emp_task_thread = EmployeeTaskThread()
        self.emp_need_thread = EmployeeNeedThread()
        self.task_service_t = TaskService(self.emp_task_thread)
        self.needs_service_t = NeedsService(self.emp_need_thread)
        self.emp_task_thread.start()
        self.emp_need_thread.start()

    def create_employee(self, x, y, name, company):
        emp = Employee(x, y, name, company)
        self.employee_list.append(emp)
        self.needs_service_t.insert_emp(emp)

    def init_extras(self):
        self.dragged_emp_i = -1
        self.previous_time = time.get_ticks()
        self.wait_time = 0.1 * 1000

    def drag_emp_if_selected(self):
        if self.dragged_emp_i != -1:
            self.employee_list[self.dragged_emp_i].rect.centerx = mouse.get_pos()[0]
            self.employee_list[self.dragged_emp_i].rect.centery = mouse.get_pos()[1]

    def pick_up_employee(self, index):
        if self.employee_list[index].rect.collidepoint(mouse.get_pos()):
            self.dragged_emp_i = index
            self.handle_emp_desk_detach_event(self.employee_list[self.dragged_emp_i])

    def put_down_employee(self, index):
        if self.employee_list[index].rect.collidepoint(mouse.get_pos()):
            self.handle_emp_desk_collide(self.employee_list[self.dragged_emp_i])
        self.dragged_emp_i = -1

    def handle_emp_desk_detach_event(self, emp):
        if emp.assigned_furniture is not None:
            emp.remove_from_desk()
            self.task_service_t.pop_emp(emp, "hunger")
            self.task_service_t.pop_emp(emp, "work")
            self.task_service_t.pop_emp(emp, "stress")

    def handle_emp_desk_collide(self, emp):
        for floor_i in range(0, len(self.room_board)):
            room_list = list(self.room_board[floor_i].values())
            for room_i in range(0, len(self.room_board[floor_i])):
                for desk_i in range(0, len(room_list[room_i].action_objects)):
                    if emp.rect.colliderect(room_list[room_i].action_objects[desk_i].rect):
                        if self.action_object_taken(room_list, room_i, desk_i) is False:
                            if type(room_list[room_i]).__name__ == "DiningRoom":
                                self.task_service_t.insert_emp(emp, "hunger")
                            elif type(room_list[room_i]).__name__ == "OfficeRoom":
                                self.task_service_t.insert_emp(emp, "work")
                            elif type(room_list[room_i]).__name__ == "GameRoom":
                                self.task_service_t.insert_emp(emp, "stress")
                            self.update_action_object_status(room_list[room_i].action_objects[desk_i])
                            emp.set_desk(room_list[room_i].action_objects[desk_i])
                            self.adjust_emp_to_action_object(emp, room_list[room_i].action_objects[desk_i], room_list[room_i], desk_i)

    def adjust_emp_to_action_object(self, emp, desk, room, desk_i):
        if type(room).__name__ == "DiningRoom":
            # print(desk_i)
            emp.rect.x = desk.rect.x
            emp.rect.y = desk.rect.y
            if desk_i % 2 != 0:
                emp.sitting_sprite_right()
                print("adjusted")
                emp.rect = emp.rect.move(-20, - 27)
            else:
                emp.sitting_sprite_left()
                emp.rect = emp.rect.move(0, - 30)
        elif type(room).__name__ == "OfficeRoom":
            emp.rect.x = desk.rect.x
            emp.rect.y = desk.rect.y
            emp.rect = emp.rect.move(10, - 10)
            emp.sitting_sprite_back()
        elif type(room).__name__ == "GameRoom":
            emp.rect.x = desk.rect.x
            emp.rect.y = desk.rect.y
            if desk_i < 2:
                emp.rect = emp.rect.move(0, -9)
                emp.sitting_sprite_back_game()
            elif desk_i == 2:
                emp.rect = emp.rect.move(7, - 25)
                emp.sitting_sprite_left()
            else:
                emp.rect = emp.rect.move(-24, - 22)
                emp.sitting_sprite_right()

    def check_employees_needs_and_move(self):
        for emp in self.employee_list:
            self.check_emp_needs_and_move(emp)
            if not emp.is_sitting_down():
                self.gravity_employee(emp)

    def check_emp_needs_and_move(self, emp: Employee):
        if emp.destination is None:
            # the moment when employee starts feeling hungry
            if emp.is_hungry():
                self.task_service_t.pop_emp(emp, "work")
                self.task_service_t.pop_emp(emp, "stress")
                self.search_for_room(emp, "DiningRoom")
            elif emp.is_stressed():
                if not emp.is_eating():
                    self.task_service_t.pop_emp(emp, "hunger")
                    self.task_service_t.pop_emp(emp, "work")
                    self.search_for_room(emp, "GameRoom")
            # when employee just stands on ground
            elif emp.is_idle():
                self.task_service_t.pop_emp(emp, "hunger")
                self.task_service_t.pop_emp(emp, "stress")
                self.search_for_room(emp, "OfficeRoom")

        # movement logic towards destination
        if emp.destination is not None and not emp.is_dragged() and self.ground.is_touching(emp):
            if emp.is_sitting_down():
                emp.remove_from_desk()
            self.move_emp_towards_destination(emp)
            if self.emp_arrived_at_destination(emp):
                self.change_destination(emp, self.search_destination(emp))

    def search_for_room(self, emp, dest_room):
        # available room searching algorithm
        for floor_i in range(0, len(self.room_board)):
            room_list = list(self.room_board[floor_i].values())

            for room_i in range(0, len(self.room_board[floor_i])):
                room_dist = 1
                # found the room the employee is in
                if emp.rect.colliderect(room_list[room_i].rect):

                    # look for the closest destination room from employee
                    while True:
                        # if we have not yet exceeded the number of rooms in list, look for rooms on right
                        if room_i + room_dist < len(room_list):
                            if type(room_list[room_i + room_dist]).__name__ == dest_room and room_list[room_i + room_dist].is_free():
                                emp.destination = room_list[room_i + room_dist]
                                break
                        # look for rooms on left
                        if room_i - room_dist > 0:
                            if type(room_list[room_i - room_dist]).__name__ == dest_room and room_list[room_i - room_dist].is_free():
                                emp.destination = room_list[room_i - room_dist]
                                break
                        if room_i + room_dist >= len(room_list) and room_i - room_dist <= 0:
                            break
                        room_dist += 1

    def search_destination(self, emp):
        # looking for a Room
        if emp.destination.__class__.__base__.__name__ == "Room":
            for action_object in emp.destination.action_objects:
                if not self.action_object_taken_by_object(action_object):
                    return action_object
        # looking for a Chair
        elif emp.destination.__class__.__base__.__name__ == "Furniture":
            emp.rect = emp.rect.move(5, 0)
            if type(emp.destination).__name__ == "OfficeDesk":
                self.task_service_t.insert_emp(emp, "work")
            elif type(emp.destination).__name__ == "DiningChair":
                self.task_service_t.insert_emp(emp, "hunger")
            elif type(emp.destination).__name__ == "GameSpot":
                self.task_service_t.insert_emp(emp, "stress")
            return None
        return emp.destination

    def change_destination(self, emp, destination):
        if destination is None:
            self.update_action_object_status(emp.destination)
            self.adjust_emp_to_action_object(emp, emp.destination, emp.destination.room,
                                             emp.destination.room.action_objects.index(emp.destination))
            emp.set_desk(emp.destination)

        emp.destination = destination

    def move_emp_towards_destination(self, emp):
        x = 0
        emp.direction = ''
        if emp.destination.rect.x > emp.rect.x + 5:
            x = 5
            emp.direction = 'R'
        elif emp.destination.rect.x < emp.rect.x - 5:
            x = -5
            emp.direction = 'L'
        emp.rect = emp.rect.move(x, 0)
        self.animate_employee(emp)

    def gravity_employee(self, emp: Employee):
        if not self.ground.is_touching(emp):
            emp.rect = emp.rect.move(0, 12)

    def emp_arrived_at_destination(self, emp):
        if not (emp.destination.rect.x > emp.rect.x + 5 or emp.destination.rect.x < emp.rect.x - 5):
            return True
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

    def animate_employee(self, employee):
        if time.get_ticks() - self.previous_time > self.wait_time:
            self.previous_time = time.get_ticks()
            if employee.direction == 'L':
                if employee.current_position == employee.WALK_LEFT:
                    employee.change_walking_sprite(employee.WALK_LEFT2)
                elif employee.current_position == employee.WALK_LEFT2:
                    employee.change_walking_sprite(employee.WALK_LEFT3)
                elif employee.current_position == employee.WALK_LEFT3:
                    employee.change_walking_sprite(employee.WALK_LEFT4)
                else:
                    employee.change_walking_sprite(employee.WALK_LEFT)
            elif employee.direction == 'R':
                if employee.current_position == employee.WALK_RIGHT:
                    employee.change_walking_sprite(employee.WALK_RIGHT2)
                elif employee.current_position == employee.WALK_RIGHT2:
                    employee.change_walking_sprite(employee.WALK_RIGHT3)
                elif employee.current_position == employee.WALK_RIGHT3:
                    employee.change_walking_sprite(employee.WALK_RIGHT4)
                else:
                    employee.change_walking_sprite(employee.WALK_RIGHT)

    def delay_by_frames(self, frames):
        delay = time.get_ticks() - self.initial_ticks
        if delay > frames:
            self.initial_ticks = time.get_ticks()
        return delay <= frames
