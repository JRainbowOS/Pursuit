def add(a, b):
    return a + b

from abc import ABC, abstractmethod
from pursuer import Pursuer
from pursued import Pursued

class Game(ABC):

    def __init__(self, chaser: Pursuer, chased: Pursued):
        self.chaser = chaser
        self.chased = chased

    @abstractmethod
    def pursue(self, num_steps):
        print('Parent class definition of Pursue')
        pass
