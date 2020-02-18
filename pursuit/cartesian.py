import numpy as np

from coordinate import Coordinate

class Cartesian2D(Coordinate):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.position = [self.x, self.y]

    def __str__(self):
        return f'Cartesian2D({self.x}, {self.y})'

    def distance_to(self, new_coord):
        assert isinstance(new_coord, Cartesian2D), 'new_coord must also be a Cartesian2D'
        squared = (new_coord.x - self.x) ** 2 + (new_coord.y - self.y) ** 2
        return np.sqrt(squared)


def main():
    coord1 = Cartesian2D(1,4)
    print(coord1)
    coord2 = Cartesian2D(3,5)

    print(coord1.distance_to(coord2))

if __name__ == '__main__':
    main()