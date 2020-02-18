from abc import ABC, abstractmethod

class Coordinate(ABC):
    """
    Generic class for coordinates
    """
    
    def __init__(self, position):
        self.position = position
        super().__init__()

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def distance_to(self, new_position):
        pass
    
