import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np 

from game import Game

from pursuer import Pursuer
from pursued import Pursued

from cat import Cat
from mouse import Mouse

class Chase(Game):
    """
    An example Game where a chaser hunts down an oblivious target 
    """

    def __init__(self, chaser: Pursuer, chased: Pursued):
        self.chaser = chaser
        self.chased = chased
        self.chased_trace_x = []
        self.chased_trace_y = []
        self.chaser_trace_x = []
        self.chaser_trace_y = []
        super().__init__(chaser, chased)

    def pursue(self, num_steps):
        """
        Run the pursuit for num_steps
        
        Arguments:
            num_steps {int} -- The number of steps to run
        """
        super().pursue(num_steps)
        # print('Child class definition of Pursue')
        for _ in range(num_steps):
            self.chased.evolve()
            chased_x = self.chased.current_position_x
            chased_y = self.chased.current_position_y
            self.chased_trace_x.append(chased_x)
            self.chased_trace_y.append(chased_y)

            self.chaser.evolve(chased_x, chased_y)
            chaser_x = self.chaser.current_position_x
            chaser_y = self.chaser.current_position_y
            self.chaser_trace_x.append(chaser_x)
            self.chaser_trace_y.append(chaser_y)

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
        ln_chaser, = ax.plot([], [], 'ro')
        ln_chased, = ax.plot([], [], 'go')
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
                      blit=True)
        plt.show()

    
    
def main():
    CAT_START = [20, 10]
    MOUSE_START = [10, 10]

    NUM_STEPS = 200

    puss = Cat(*CAT_START)
    muss = Mouse(*MOUSE_START)

    chase = Chase(puss, muss)
    chase.pursue(NUM_STEPS)

    chase.animate()

if __name__ == '__main__':
    main()