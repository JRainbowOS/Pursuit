from abc import ABC, abstractmethod

from coordinate import Coordinate
from cartesian import Cartesian2D

class Chaser(ABC):
    """
    Generic class for pursuit animals
    """

    _dt = 1

    def __init__(self, initial_coordinate: Coordinate, initial_speed):
        self.position = initial_coordinate.position
        self.speed = initial_speed
        super().__init__()

    @abstractmethod
    def step(self, other_coordinate: Coordinate):
        """
        Chase pursued object by one time step
        
        Arguments:
            pursued_position_x {float} -- current x position of pursued
            pursued_position_y {float} -- current y position of pursued
        """
        pass
