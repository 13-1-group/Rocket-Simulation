import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from .utils import plot_initialize, plot_show
from .Orbit import Orbit


class Hyperbolic(Orbit):
    def __init__(self, a, e):
        self.p1_a, self.p1_e = a, e

        self.t = np.linspace(np.pi / 2, 3 * np.pi / 2, 361)
        self.x1 = np.sqrt(self.p1_a * 1 / (np.cos(2 * self.t) + 0.01)) * np.cos(self.t)
        self.y1 = np.sqrt(self.p1_a * 1 / (np.cos(2 * self.t) + 0.01)) * np.sin(self.t)

    def solar_system(self, i):
        self.rocket.set_data(self.x1[i], self.y1[i])
        self.rocket_o.set_data(self.x1[:i], self.y1[:i])
        return self.rocket, self.rocket_o

    def visualize(self):
        fig, ax, self.rocket, self.rocket_o = plot_initialize()

        anim = animation.FuncAnimation(fig, self.solar_system, frames=len(self.t), interval=25, blit=True,
                                       repeat=True)
        fig.patch.set_facecolor('k')
        fig.tight_layout()
        plt.plot(self.p1_a * self.p1_e, 0, 'yo', markersize=6.5, label='Moon')
        plot_show()
