from matplotlib.animation import writers
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

BOUNDS_X = (-20.2, 20.2)
BOUNDS_Y = (-20.2, 20.2)


class Ellipsis:
    def __init__(self, e, a):
        self.p1_a, self.p1_e = a, e
        p1_b = self.p1_a * np.sqrt(1 - self.p1_e ** 2)

        self.fig = plt.figure()
        self.ax = plt.axes(xlim=BOUNDS_X, ylim=BOUNDS_Y)

        self.rocket, = self.ax.plot([], [], marker='o', markersize=4, markerfacecolor='red', label='Rocket')
        self.rocket_o, = self.ax.plot([], [], color='w', lw=1.5)

        self.t = np.linspace(0, 2 * np.pi, 361)
        self.x1 = self.p1_a * np.cos(self.t) - self.p1_a * self.p1_e
        self.y1 = p1_b * np.sin(self.t)

    def solar_system(self, i):
        self.rocket.set_data(self.x1[i], self.y1[i])
        self.rocket_o.set_data(self.x1[:i], self.y1[:i])
        return self.rocket, self.rocket_o

    def visualize(self):
        anim = animation.FuncAnimation(self.fig, self.solar_system, frames=len(self.t), interval=25, blit=True,
                                       repeat=True)
        self.fig.patch.set_facecolor('k')
        self.fig.tight_layout()
        plt.plot(self.p1_a * self.p1_e, 0, 'yo', markersize=6.5, label='Moon')
        plt.axis(False)
        plt.legend()
        plt.show()


if __name__ == '__main__':
    el = Ellipsis(0.1, 2)
    el.visualize()
