from pursued import Pursued

class Mouse(Pursued):

    def __init__(self, current_position_x, current_position_y, speed):
        self.current_position_x = current_position_x
        self.current_position_y = current_position_y
        self.speed = speed

    def evolve(self):
        super().evolve()
        print(f'Time step is {self._dt}')


def main():

    START_POSITION = [0,0]
    PURSUED_SPEED = 1

    stuart = Mouse(*START_POSITION, PURSUED_SPEED)
    stuart.evolve()
    print(stuart)

if __name__ == '__main__':
    main()