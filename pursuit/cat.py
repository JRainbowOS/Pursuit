import numpy as np 

from pursuer import Pursuer
from utils import make_unit_vector

class Cat(Pursuer):
    """
    Simple chaser subclass
    """

    SPEED = 0.5
    SPEED_INC = 0.0

    def __init__(self, initial_position_x, initial_position_y):
        self.current_position_x = initial_position_x
        self.current_position_y = initial_position_y
        self.speed = self.speed_generator(Cat.SPEED, Cat.SPEED_INC)

    def evolve(self, pursued_position_x, pursued_position_y):
        super().evolve(pursued_position_x, pursued_position_y)
        # print(f'Time step is {self._dt}')
        speed = next(self.speed)

        dx, dy = self.get_movement_vector(self.current_position_x,
                                          self.current_position_y,
                                          pursued_position_x,
                                          pursued_position_y,
                                          speed,
                                          self._dt)

        self.current_position_x += dx
        self.current_position_y += dy

    @staticmethod
    def speed_generator(initial_speed, increment):
        speed = initial_speed
        while True:
            yield speed 
            speed += increment

    @staticmethod
    def get_movement_vector(current_position_x,
                            current_position_y,
                            pursued_position_x,
                            pursued_position_y,
                            speed,
                            dt):
        x_change = pursued_position_x - current_position_x
        y_change = pursued_position_y - current_position_y

        dx, dy = make_unit_vector(x_change, y_change)

        return [dx * speed * dt, dy * speed * dt]
        
        
def main():

    START_POSITION = [0,0]
    PURSUED_POSITION = [10,10]

    lola = Cat(*START_POSITION)
    for _ in range(100):
        lola.evolve(*PURSUED_POSITION)
        print(lola.current_position_x, lola.current_position_y)

if __name__ == '__main__':
    main()