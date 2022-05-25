import matplotlib.pyplot as plt
from .constants import BOUNDS_X, BOUNDS_Y


def plot_initialize():
    """
    initialize plot and solar system objects
    :return: plot figure, plot axes, rocket and rocket_o - solar system objects
    """
    fig = plt.figure()
    ax = plt.axes(xlim=BOUNDS_X, ylim=BOUNDS_Y)

    rocket, = ax.plot([], [], marker='o', markersize=4, markerfacecolor='red', label='Rocket')
    rocket_o, = ax.plot([], [], color='w', lw=1.5)

    return fig, ax, rocket, rocket_o


def plot_show():
    """
        draw plot in separate window
        """
    plt.axis(False)
    plt.legend()
    plt.show()
