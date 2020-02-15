from pursuer import Pursuer

class Cat(Pursuer):

    def __init__(self, current_position_x, current_position_y, speed):
        self.current_position_x = current_position_x
        self.current_position_y = current_position_y
        self.speed = speed

    def evolve(self, pursued_position_x, pursued_position_y):
        super().evolve(pursued_position_x, pursued_position_y)
        print(f'Time step is {self._dt}')


def main():

    START_POSITION = [0,0]
    PURSUED_POSITION = [1,1]
    PURSUER_SPEED = 1

    lola = Cat(*START_POSITION, PURSUER_SPEED)
    lola.evolve(*PURSUED_POSITION)

if __name__ == '__main__':
    main()