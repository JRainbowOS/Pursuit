import numpy as np

from chaser import Chaser
from cartesian import Cartesian2D

class Mole(Chaser):
    """
    Moles blindly move in a random walk
    """
    MAX_CURVATURE = np.pi / 6
    SPEED = 1

    def __init__(self, position: Cartesian2D):
        self.position = position
        self.bearing = 2 * np.pi * np.random.random()

    def step(self, other_coordinate):
        dx, dy = self._find_displacement()
        self.position.x += dx
        self.position.y += dy
        return self.position

    def _find_displacement(self):
        angle_inc = Mole._get_random_angle()
        new_bearing = self.bearing + angle_inc
        self.bearing = new_bearing
        dx = Mole._dt * Mole.SPEED * np.cos(new_bearing)
        dy = Mole._dt * Mole.SPEED * np.sin(new_bearing)
        return dx, dy

    @classmethod
    def _get_random_angle(cls):
        angle = np.random.normal(0, cls.MAX_CURVATURE)
        return angle


def main():
    INITIAL_COORDINATE = Cartesian2D(1, 1)
    other_coordinate = Cartesian2D(10, 10)

    holy_moly = Mole(INITIAL_COORDINATE)
    new_coordinate = holy_moly.step(other_coordinate)
    new_coordinate = holy_moly.step(other_coordinate)


if __name__ == '__main__':
    main()