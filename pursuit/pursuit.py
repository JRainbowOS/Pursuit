from game import Game
from chaser import Chaser

from cartesian import Cartesian2D
from rat import Rat

class Pursuit(Game):

    def __init__(self, chaser: Rat, chased: Rat):
        super().__init__(chaser, chased)
        self.chaser = chaser
        self.chased = chased


    def play(self):
        current_chaser_position = self.chaser.position
        current_chased_position = self.chased.position

        steps_taken = 0
        separation = current_chaser_position.distance_to(current_chased_position)
        while separation > self.chaser.PAW_DISTANCE:
            new_chaser_position = self.chaser.step(current_chased_position)
            new_chased_position = self.chased.step(current_chaser_position)

            self.chaser.position = new_chaser_position
            self.chased.position = new_chased_position

            steps_taken += 1
            separation = new_chaser_position.distance_to(new_chased_position)

        print(f'Rat has been caught in {steps_taken} steps!')
             

def main():
    REMI_START = Cartesian2D(0, 0)

    FEMI_START = Cartesian2D(10, 100)

    remi = Rat(REMI_START)
    femi = Rat(FEMI_START)

    pursuit = Pursuit(remi, femi)

    pursuit.play()

if __name__ == '__main__':
    main()

