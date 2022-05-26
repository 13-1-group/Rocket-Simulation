import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from .utils import plot_initialize, plot_show
from .Orbit import Orbit


class Ellipsis(Orbit):
    """
    Ellipsis Orbit Rocket Class

    Methods:
        solar_system(i):
            transmits the coordinates of the rocket's movement.
        visualize():
            rendering of the animated movement of the rocket around the celestial body.
    """

    def __init__(self, e, a):
        """
        Initializes the parameters of the elliptical orbit and calculates the coordinates of the rocket's movement.

        :param e: eccentricity
        :type e: float
        :param a: semiaxis
        :type a: float

        """
        self.p1_a, self.p1_e = a, e
        if (1 - self.p1_e ** 2) < 0:
            raise ArithmeticError('Wrong eccentricity value. Root value is less than zero.')
        p1_b = self.p1_a * np.sqrt(1 - self.p1_e ** 2)

        self.t = np.linspace(0, 2 * np.pi, 361)
        self.x1 = self.p1_a * np.cos(self.t) - self.p1_a * self.p1_e
        self.y1 = p1_b * np.sin(self.t)

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
