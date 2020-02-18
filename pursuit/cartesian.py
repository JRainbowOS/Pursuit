import numpy as np

from coordinate import Coordinate

class Cartesian2D(Coordinate):

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return f'Cartesian2D({self.x}, {self.y})'


    def distance_to(self, new_coord):
        assert isinstance(new_coord, Cartesian2D), 'new_coord must also be a Cartesian2D'
        squared = (new_coord.x - self.x) ** 2 + (new_coord.y - self.y) ** 2
        return np.sqrt(squared)


    def angle_to(self, new_coord):
        assert isinstance(new_coord, Cartesian2D), 'new_coord must also be a Cartesian2D'
        dx = new_coord.x - self.x
        dy = new_coord.y - self.y
        theta = np.arctan2(dy, dx)
        return theta


    def get_unit_vector(self, new_coord):
        assert isinstance(new_coord, Cartesian2D), 'new_coord must also be a Cartesian2D'
        dx = new_coord.x - self.x
        dy = new_coord.y - self.y
        norm = np.sqrt(dx ** 2 + dy ** 2)
        return dx / norm, dy / norm


def main():
    coord1 = Cartesian2D(1,1)
    print(coord1)
    coord2 = Cartesian2D(1,0)

    print(coord1.angle_to(coord2))
    print(coord1.get_unit_vector(coord2))

if __name__ == '__main__':
    main()