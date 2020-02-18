from chaser import Chaser
from cartesian import Cartesian2D

class Rat(Chaser):
    """
    Rats are not afraid of anything and will investigate any chaser / chased
    """

    def __init__(self, initial_coordinate: Cartesian2D, initial_speed):
        super().__init__(initial_coordinate, initial_speed)

    def step(self, other_coordinate):
        pass
    
def main():
    INITIAL_COORDINATE = Cartesian2D(1,1)
    INITIAL_SPEED = 1

    remi = Rat(INITIAL_COORDINATE, INITIAL_SPEED)

if __name__ == '__main__':
    main()