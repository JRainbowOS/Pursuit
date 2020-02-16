from abc import ABC, abstractmethod

class Pursuer(ABC):
    """
    Generic pursuer class for chasing pursued
    """

    _dt = 1

    def __init__(self, current_position_x, current_position_y, speed):
        self.current_position_x = current_position_x
        self.current_position_y = current_position_y
        self.speed = speed
        super().__init__()

    @abstractmethod
    def evolve(self, pursued_position_x, pursued_position_y):
        """
        Chase pursued object by one time step
        
        Arguments:
            pursued_position_x {float} -- current x position of pursued
            pursued_position_y {float} -- current y position of pursued
        """
        # print('Evolving using parent method')
        pass