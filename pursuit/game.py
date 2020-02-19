from abc import ABC, abstractmethod
from chaser import Chaser

class Game(ABC):
    """
    Generic Game Object
    """

    def __init__(self, chaser: Chaser, chased: Chaser):
        self.chaser = chaser
        self.chased = chased
        assert chaser._dt == chased._dt, """
        Time increments should be the same for chaser and chased
        """

    @abstractmethod
    def play(self):
        """
        Runs one step of the game
        """
        pass
