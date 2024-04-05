from model.Employee.Employee import Employee
from model.Room import Room
from service.EmployeeServices.Needs.TaskService import TaskService


class DestinationSearchService:
    def __init__(self, room_board: dict, task_service_t: TaskService):
        self.room_board = room_board
        self.ELEVATOR_POSITION = 3
        self.task_service_t = task_service_t

    def search_for_room(self, emp, dest_room: str):
        # available room searching algorithm
        for floor_i in range(0, len(self.room_board)):
            room_list = list(self.room_board[floor_i])

            for room_i in range(0, len(self.room_board[floor_i])):
                room_dist = 1
                # found the room the employee is in
                if emp.rect.colliderect(room_list[room_i].rect):
                    emp.floor = floor_i
                # look for the closest destination room from employee
                while True:
                    # if we have not yet exceeded the number of rooms in list, look for rooms on right
                    if room_i + room_dist < len(room_list):
                        if type(room_list[room_i + room_dist]).__name__ == dest_room and room_list[room_i + room_dist].is_free():
                            if self.is_on_different_floor(emp, floor_i):
                                emp.destination_mem = room_list[room_i + room_dist]
                                emp.destination = self.room_board[emp.floor][self.ELEVATOR_POSITION]
                            else:
                                emp.destination = room_list[room_i + room_dist]
                            return
                    # look for rooms on left
                    if room_i - room_dist >= 0:
                        if type(room_list[room_i - room_dist]).__name__ == dest_room and room_list[room_i - room_dist].is_free():
                            if self.is_on_different_floor(emp, floor_i):
                                emp.destination_mem = room_list[room_i - room_dist]
                                emp.destination = self.room_board[emp.floor][self.ELEVATOR_POSITION]
                            else:
                                emp.destination = room_list[room_i - room_dist]
                            return
                    if room_i + room_dist >= len(room_list) and room_i - room_dist < 0:
                        break
                    room_dist += 1

    def is_on_different_floor(self, emp, floor_i):
        return emp.floor != floor_i

    def search_for_spot(self, emp: Employee):
        # looking for a spot
        if emp.destination.__class__.__base__.__name__ == "Room":
            for action_object in emp.destination.action_objects:
                if not self.action_object_taken_by_object(action_object):
                    return action_object
        # sit on the spot
        elif emp.destination.__class__.__base__.__name__ == "Furniture" and not emp.destination.taken:
            emp.rect = emp.rect.move(5, 0)
            if type(emp.destination).__name__ == "OfficeDesk":
                self.task_service_t.insert_emp(emp, "work")
            elif type(emp.destination).__name__ == "DiningChair":
                self.task_service_t.insert_emp(emp, "hunger")
            elif type(emp.destination).__name__ == "GameSpot":
                self.task_service_t.insert_emp(emp, "stress")
            elif type(emp.destination).__name__ == "Elevator":
                self.teleport_to_floor(emp, emp.destination_mem)
                self.change_destination(emp, emp.destination_mem)
                emp.clear_destination_mem()
                emp.floor = emp.destination.floor
                emp.destination = self.search_for_spot(emp)
                return emp.destination
            return None
        else:
            # in case when employee's destination spot became taken before he managed to arrive
            for action_object in emp.destination.room.action_objects:
                if not self.action_object_taken_by_object(action_object):
                    return action_object
            # if no other desks in the room are free, look for a different room
            self.search_for_room(emp, type(emp.destination.room).__name__)
            if emp.destination.__class__.__base__.__name__ != "Room":
                raise Exception("There is more employees than possible desks, so the destination searching failed")
            self.change_destination(emp, self.search_for_spot(emp))
        return emp.destination

    def teleport_to_floor(self, emp: Employee, room: Room):
        emp.rect.y = room.rect.y + room.rect.height - emp.rect.height

    def change_destination(self, emp, destination):
        emp.destination = destination

    def emp_arrived_at_destination(self, emp):
        if not (emp.destination.rect.x > emp.rect.x + 5 or emp.destination.rect.x < emp.rect.x - 5):
            return True
        return False

    def action_object_taken_by_object(self, action_object):
        return action_object.taken
