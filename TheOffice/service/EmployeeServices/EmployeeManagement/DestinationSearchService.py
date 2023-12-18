from service.EmployeeServices.EmployeeManagement.CollisionService import CollisionService
from service.EmployeeServices.Needs.TaskService import TaskService

class DestinationSearchService:
    def __init__(self, room_board : dict, task_service_t : TaskService):
        self.room_board = room_board
        self.task_service_t = task_service_t
        self.adjust_emp_to_action_object = CollisionService.adjust_emp_to_action_object
        self.update_action_object_status = CollisionService.update_action_object_status

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

    def emp_arrived_at_destination(self, emp):
        if not (emp.destination.rect.x > emp.rect.x + 5 or emp.destination.rect.x < emp.rect.x - 5):
            return True
        return False

    def action_object_taken_by_object(self, action_object):
        return action_object.taken
