import matplotlib.pyplot as plt

from game import Game

from pursuer import Pursuer
from pursued import Pursued

from cat import Cat
from mouse import Mouse

class Chase(Game):

    def __init__(self, chaser: Pursuer, chased: Pursued):
        self.chaser = chaser
        self.chased = chased

    def pursue(self, num_steps, display=True):
        super().pursue(num_steps)
        print('Child class definition of Pursue')
        for _ in range(num_steps):
            self.chased.evolve()
            chased_x = self.chased.current_position_x
            chased_y = self.chased.current_position_y
            self.chaser.evolve(chased_x, chased_y)
    
    
def main():
    CAT_START = [0, 0]
    MOUSE_START = [10, 10]

    puss = Cat(*CAT_START)
    muss = Mouse(*MOUSE_START)

    chase = Chase(puss, muss)
    chase.pursue(10)

if __name__ == '__main__':
    main()