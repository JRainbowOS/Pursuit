from abc import ABC, abstractmethod

class Pursued(ABC):
    """
    Generic object that is being chased
    """

    _dt = 1

    def __init__(self, current_position_x, current_position_y, speed):
        self.current_position_x = current_position_x
        self.current_position_y = current_position_y
        self.speed = speed
        super().__init__()

    @abstractmethod
    def evolve(self):
        """
        Move forward by one time step
        """
        # print('Evolving using parent method')
        pass