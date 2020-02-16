import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np 

from game import Game

from pursuer import Pursuer
from pursued import Pursued

from cat import Cat
from mouse import Mouse

class Chase(Game):

    def __init__(self, chaser: Pursuer, chased: Pursued):
        self.chaser = chaser
        self.chased = chased
        self.chased_trace_x = []
        self.chased_trace_y = []
        self.chaser_trace_x = []
        self.chaser_trace_y = []
        super().__init__(chaser, chased)

    def pursue(self, num_steps):
        super().pursue(num_steps)
        print('Child class definition of Pursue')
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


    def display(self):
        plt.plot(self.chased_trace_x, self.chased_trace_y)
        plt.plot(self.chaser_trace_x, self.chaser_trace_y)

        plt.show()

    @staticmethod
    def init_animation():
        fig, ax = plt.subplots()
        xdata, ydata = [], []
        ln, = plt.plot([], [], 'ro')
        return ln, 

    @staticmethod
    def update_animation(x_frame):
        xdata.append(x_frame)
        ydata.append(y_frame)
        ln.set_data(xdata, ydata)
        return ln,

    def animate(self):

        fig, ax = plt.subplots()
        xdata, ydata = [], []
        ln, = plt.plot([], [], 'ro')

        def init_animation():
            # bounds could live here
            return ln,

        def update_animation(frame):
            xdata.append(frame)
            ydata.append(np.sin(frame))
            ln.set_data(xdata, ydata)
            return ln,

        ani = FuncAnimation(fig, 
                            update_animation,
                            frames=np.linspace(0, 2*np.pi, 128),
                            init_func=init_animation,
                            blit=True)
        plt.show()

    
    
def main():
    CAT_START = [0, 0]
    MOUSE_START = [10, 10]

    puss = Cat(*CAT_START)
    muss = Mouse(*MOUSE_START)

    chase = Chase(puss, muss)
    chase.pursue(100)

    chase.display()
    chase.animate()

if __name__ == '__main__':
    main()