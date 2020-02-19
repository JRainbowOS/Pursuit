def add(a, b):
    return a + b

from abc import ABC, abstractmethod
from pursuer import Pursuer
from pursued import Pursued

class Game(ABC):
    """
    Generic Game Object
    """

    def __init__(self, chaser: Pursuer, chased: Pursued):
        self.chaser = chaser
        self.chased = chased
        assert chaser._dt == chased._dt, """
        Time increments should be the same for chaser and chased
        """

    @abstractmethod
    def pursue(self, num_steps):
        """
        Runs a pursuit for num_steps
        
        Arguments:
            num_steps {int} -- Number of time steps to process
        """
        # print('Parent class definition of Pursue')
        pass
