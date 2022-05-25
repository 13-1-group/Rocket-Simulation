import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from .utils import plot_initialize, plot_show
from .Orbit import Orbit


class Parabolic(Orbit):
    def __init__(self, p):
        self.p1_p = p

        self.t = np.linspace(-np.pi / 2 + 0.0001, np.pi / 2 - 0.0001, 361)[::-1]

        self.x1 = self.p1_p / (1 - np.sin(self.t)) * np.cos(self.t)
        self.y1 = self.p1_p / (1 - np.sin(self.t)) * np.sin(self.t)
        self.x1 = np.array(list(-1 * self.x1) + list(self.x1[::-1]))
        self.y1 = np.array(list(self.y1) + list(self.y1[::-1]))

    def solar_system(self, i):
        self.rocket.set_data(self.x1[i], self.y1[i])
        self.rocket_o.set_data(self.x1[:i], self.y1[:i])
        return self.rocket, self.rocket_o

    def visualize(self):
        fig, ax, self.rocket, self.rocket_o = plot_initialize()

        anim = animation.FuncAnimation(fig, self.solar_system, frames=2 * len(self.t), interval=25, blit=True,
                                       repeat=True)
        fig.patch.set_facecolor('k')
        fig.tight_layout()
        plt.plot(0, self.p1_p / (1 - np.sin(3 * np.pi / 2)) * np.sin(3 * np.pi / 2) + self.p1_p / 2, 'yo',
                 markersize=6.5, label='Moon')
        plot_show()
