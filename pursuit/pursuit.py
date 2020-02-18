from game import Game
from chaser import Chaser

from cartesian import Cartesian2D
from rat import Rat

class Pursuit(Game):

    def __init__(self, chaser: Rat, chased: Rat):
        super().__init__()
        self.chaser = chaser
        self.chased = chased

    def play(self):
        current_chaser_position = self.chaser.position
        current_chased_position = self.chased.position

        new_chaser_position = self.chaser.step(current_chased_position)
        new_chased_position = self.chased.step(current_chaser_position)

        pass 

def main():
    REMI_START = Cartesian2D(0, 0)
    REMI_SPEED = 1

    FEMI_START = Cartesian2D(1, 1)
    FEMI_SPEED = 1

    remi = Rat(REMI_START, REMI_SPEED)
    femi = Rat(FEMI_START, FEMI_SPEED)

    pursuit = Pursuit(remi, femi)

    pursuit.play()

if __name__ == '__main__':
    main()

