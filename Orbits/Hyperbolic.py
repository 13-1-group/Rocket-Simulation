import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from .utils import plot_initialize, plot_show
from .Orbit import Orbit


class Hyperbolic(Orbit):
    """
    Hyperbolic Orbit Rocket Class

    Methods:
        solar_system(i):
            transmits the coordinates of the rocket's movement.
        visualize():
            rendering of the animated movement of the rocket around the celestial body.
    """

    def __init__(self, e, a):
        """
        Initializes the parameters of the hyperbolic orbit and calculates the coordinates of the rocket's motion.

        :param e: eccentricity
        :type e: float
        :param a: semiaxis
        :type a: float
        """
        self.p1_a, self.p1_e = a, e
        err = 1e10-8

        self.t = np.linspace(np.pi / 2, 3 * np.pi / 2, 361)
        denom_value = np.cos(2 * self.t)
        denom_value[denom_value == 0] = err
        root_value = self.p1_a * 1 / denom_value
        root_value[root_value < 0] = None
        self.x1 = np.sqrt(root_value) * np.cos(self.t)
        self.y1 = np.sqrt(root_value) * np.sin(self.t)

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
        plt.plot(self.p1_a / self.p1_e, 0, 'yo', markersize=6.5, label='Moon')
        plot_show()
