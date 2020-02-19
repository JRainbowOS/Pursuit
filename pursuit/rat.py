from chaser import Chaser
from cartesian import Cartesian2D

class Rat(Chaser):
    """
    Rats are not afraid of anything and will investigate any chaser / chased
    """
    PAW_DISTANCE = 1
    SPEED = 1

    def __init__(self, position: Cartesian2D):
        self.position = position

    def step(self, other_coordinate):
        dx, dy = self._find_displacement(other_coordinate)
        self.position.x += dx
        self.position.y += dy
        return self.position

        
    def _find_displacement(self, other_coordinate):
        unit_x, unit_y = self.position.get_unit_vector(other_coordinate)
        dx = Rat.SPEED * Rat._dt * unit_x 
        dy = Rat.SPEED * Rat._dt * unit_y 
        return dx, dy        



def main():
    INITIAL_COORDINATE = Cartesian2D(1, 1)
    other_coordinate = Cartesian2D(10, 10)

    remi = Rat(INITIAL_COORDINATE)
    print(remi)
    new_coordinate = remi.step(other_coordinate)
    new_coordinate = remi.step(other_coordinate)


if __name__ == '__main__':
    main()