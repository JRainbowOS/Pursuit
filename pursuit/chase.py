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
        self.chased_trace = []
        self.chaser_trace = []
        super().__init__(chaser, chased)

    def pursue(self, num_steps):
        super().pursue(num_steps)
        print('Child class definition of Pursue')
        for _ in range(num_steps):
            self.chased.evolve()
            chased_x = self.chased.current_position_x
            chased_y = self.chased.current_position_y
            self.chased_trace.append([chased_x, chased_y])

            self.chaser.evolve(chased_x, chased_y)
            chaser_x = self.chaser.current_position_x
            chaser_y = self.chaser.current_position_y
            self.chaser_trace.append([chaser_x, chaser_y])

    def display(self):
        pass

    
    
def main():
    CAT_START = [0, 0]
    MOUSE_START = [10, 10]

    puss = Cat(*CAT_START)
    muss = Mouse(*MOUSE_START)

    chase = Chase(puss, muss)
    chase.pursue(10)

if __name__ == '__main__':
    main()