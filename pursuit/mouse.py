import numpy as np
import matplotlib.pyplot as plt 

from pursued import Pursued

class Mouse(Pursued):
    """
    Simple pursued object subclass to be chased by Cat
    """

    SPEED = 1
    SPEED_INC = 0
    INITIAL_ANGLE = 0
    ANGLE_INC = 0.1

    def __init__(self, initial_position_x, initial_position_y):
        self.current_position_x = initial_position_x
        self.current_position_y = initial_position_y
        self.speed = self.speed_generator(Mouse.SPEED, Mouse.SPEED_INC)
        self.angle = self.angle_generator(Mouse.INITIAL_ANGLE, Mouse.ANGLE_INC)

    def evolve(self):
        super().evolve()
        # print(f'Time step is {self._dt}')
        angle = next(self.angle)
        speed = next(self.speed)

        dx, dy = self.get_movement_vector(angle, speed, self._dt)
        self.current_position_x += dx
        self.current_position_y += dy        

    @staticmethod
    def angle_generator(initial_angle, increment):
        angle = initial_angle
        while True:
            yield angle % (2 * np.pi)
            angle += increment

    @staticmethod
    def random_angle_generator(initial_angle, max_curvature):
        angle = initial_angle
        while True:
            pass


    @staticmethod
    def speed_generator(initial_speed, increment):
        speed = initial_speed
        while True:
            yield speed 
            speed += increment

    @staticmethod
    def get_movement_vector(angle, speed, dt):
        dx = np.sin(angle)
        dy = np.cos(angle)
        return [dx * speed * dt, dy * speed * dt]



def main():

    START_POSITION = [0,0]
    rambil = Mouse(*START_POSITION)
    
    s = []
    t = []
    for _ in range(100):
        rambil.evolve()
        x = rambil.current_position_x
        y = rambil.current_position_y
        s.append(x)
        t.append(y)
        print(x, y)

    plt.plot(s, t)
    plt.show()

if __name__ == '__main__':
    main()