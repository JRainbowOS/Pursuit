import numpy as np

from pursued import Pursued

class Mouse(Pursued):

    SPEED = 1
    INITIAL_DIRECTION_VECTOR = np.array([1, 0])

    def __init__(self, current_position_x, current_position_y):
        self.current_position_x = current_position_x
        self.current_position_y = current_position_y
        self.speed = Mouse.SPEED

    def evolve(self):
        super().evolve()
        print(f'Time step is {self._dt}')
        direction_vector = next(self.direction_generator(1, 0))
        print(direction_vector)

    @staticmethod
    def direction_generator(dx, dy):
        direction_vector = np.array([0, 1])
        while True:
            yield direction_vector + np.array([dx, dy])



def main():

    START_POSITION = [0,0]
    PURSUED_SPEED = 1

    stuart = Mouse(*START_POSITION)
    stuart.evolve()
    stuart.evolve()
    # print(stuart)

if __name__ == '__main__':
    main()