import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from game import Game
from chaser import Chaser

from cartesian import Cartesian2D
from rat import Rat
from mole import Mole

class Pursuit(Game):

    def __init__(self, chaser: Rat, chased: Mole):
        super().__init__(chaser, chased)
        self.chaser = chaser
        self.chased = chased
        self.chased_trace_x = []
        self.chased_trace_y = []
        self.chaser_trace_x = []
        self.chaser_trace_y = []

    def play(self):
        """
        Play game until chased is caught by chaser
        """
        current_chaser_position = self.chaser.position
        current_chased_position = self.chased.position

        steps_taken = 0
        separation = current_chaser_position.distance_to(current_chased_position)
        while separation > self.chaser.PAW_DISTANCE:
            new_chaser_position = self.chaser.step(current_chased_position)
            new_chased_position = self.chased.step(current_chaser_position)

            self._update_positions(current_chaser_position, current_chased_position)

            steps_taken += 1
            separation = new_chaser_position.distance_to(new_chased_position)

        print(f'Pursuit has ended after {steps_taken} steps!')

    def _update_positions(self, chaser_position: Cartesian2D, chased_position: Cartesian2D):
        """Update the positions of the chased and chaser
        
        Arguments:
            chaser_position {Cartesian2D} -- Current position of the chaser
            chased_position {Cartesian2D} -- Current position of the chased
        """
        self.chaser.position = chaser_position
        self.chaser_trace_x.append(chaser_position.x)
        self.chaser_trace_y.append(chaser_position.y)

        self.chased.position = chased_position
        self.chased_trace_x.append(chased_position.x)        
        self.chased_trace_y.append(chased_position.y)        

    def _get_extents(self, margin):
        """
        Returns the extents for plotting the animation
        
        Arguments:
            margin {int} -- Buffer size around the plot
        
        Returns:
            tuple -- (min_x, min_y, max_x, max_y)
        """
        min_x = min(min(self.chased_trace_x), min(self.chaser_trace_x))
        max_x = max(max(self.chased_trace_x), max(self.chaser_trace_x))

        min_y = min(min(self.chased_trace_y), min(self.chaser_trace_y))
        max_y = max(max(self.chased_trace_y), max(self.chaser_trace_y))

        return min_x - margin, min_y - margin, max_x + margin, max_y + margin

    def display(self):
        """
        Display trajectories of pursuit
        """
        plt.plot(self.chased_trace_x, self.chased_trace_y)
        plt.plot(self.chaser_trace_x, self.chaser_trace_y)
        plt.show()

    def animate(self):
        """
        Produce an animation of the pursuit processed so far
        """
        dt = self.chaser._dt
        MARGIN = 5
        min_x, min_y, max_x, max_y = self._get_extents(margin=MARGIN)

        fig = plt.figure()
        ax = fig.add_subplot(111, autoscale_on=False, xlim=(min_x, max_x),
                                                      ylim=(min_y, max_y))
        ax.set_aspect('equal')

        chaser_xdata, chaser_ydata = [], []
        chased_xdata, chased_ydata = [], []
        ln_chaser, = ax.plot([], [], 'r', linewidth=2, markersize=0)
        ln_chased, = ax.plot([], [], 'g', linewidth=2, markersize=0)
        time_template = 'time = %.1fs'
        time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

        def init_animation():
            ln_chaser.set_data([], [])
            ln_chased.set_data([], [])
            time_text.set_text('')
            return ln_chaser, ln_chased, time_text

        def animate(i):
            chaser_xdata.append(self.chaser_trace_x[i])
            chaser_ydata.append(self.chaser_trace_y[i])

            chased_xdata.append(self.chased_trace_x[i])
            chased_ydata.append(self.chased_trace_y[i])

            ln_chaser.set_data(chaser_xdata, chaser_ydata)
            ln_chased.set_data(chased_xdata, chased_ydata)

            time_text.set_text(time_template % (i * dt))

            return ln_chaser, ln_chased, time_text

        FuncAnimation(fig, 
                      animate,
                      len(self.chaser_trace_x),
                      init_func=init_animation,
                      interval=100,
                      blit=True,
                      repeat=False)
        plt.show()

def main():
    REMI_START = Cartesian2D(0, 0)

    FEMI_START = Cartesian2D(20, 20)

    remi = Rat(REMI_START)
    femi = Mole(FEMI_START)

    pursuit = Pursuit(remi, femi)

    pursuit.play()

    pursuit.animate()

if __name__ == '__main__':
    main()

