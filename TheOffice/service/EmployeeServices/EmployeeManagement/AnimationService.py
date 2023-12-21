from pygame import time


class AnimationService:
    def __init__(self):
        self.wait_time = 0.1 * 1000
        self.previous_time_map = {}

    def animate_employee(self, employee):
        if not self.previous_time_map.__contains__(id(employee)):
            self.previous_time_map[id(employee)] = time.get_ticks()
        if time.get_ticks() - self.previous_time_map[id(employee)] > self.wait_time:
            self.previous_time_map[id(employee)] = time.get_ticks()
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
