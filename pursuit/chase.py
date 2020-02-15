from game import Game

from pursuer import Pursuer
from pursued import Pursued

from cat import Cat
from mouse import Mouse

class Chase(Game):

    def __init__(self, chaser: Pursuer, chased: Pursued):
        self.chaser = chaser
        self.chased = chased

    def pursue(self, num_steps):
        pass

    
    
def main():
    CAT_START = [0, 0]
    MOUSE_START = [1, 1]
    CAT_SPEED = 2
    MOUSE_SPEED = 1

    puss = Cat(*CAT_START, CAT_SPEED)
    muss = Mouse(*MOUSE_START, MOUSE_SPEED)

    chase = Chase(muss, puss)

if __name__ == '__main__':
    main()