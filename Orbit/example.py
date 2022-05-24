from matplotlib.animation import writers
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

BOUNDS_X = (-20.2, 20.2)
BOUNDS_Y = (-20.2, 20.2)

# Semimajor and semiminor distances of planet's and comet's orbit are in AU
p1_a, p1_e = 1, 0.001
p1_b = p1_a * np.sqrt(1 - p1_e ** 2)
# p1_p =

fig = plt.figure()
ax = plt.axes(xlim=BOUNDS_X, ylim=BOUNDS_Y)

rocket, = ax.plot([], [], marker='o', markersize=4, markerfacecolor='red', label='Rocket')
rocket_o, = ax.plot([], [], color='w', lw=1.5)

t = np.linspace(0, 2 * np.pi, 361)
x1 = p1_a * np.cos(t) - p1_a * p1_e
y1 = p1_b * np.sin(t)


def solar_system(i):
    rocket.set_data(x1[i], y1[i])
    rocket_o.set_data(x1[:i], y1[:i])
    return rocket, rocket_o


# def parabolic(i)

anim = animation.FuncAnimation(fig, solar_system, frames=len(t), interval=25, blit=True, repeat=True)
fig.patch.set_facecolor('k')
fig.tight_layout()
plt.plot(p1_a * p1_e, 0, 'yo', markersize=6.5, label='Moon')
plt.axis(False)
plt.legend()
plt.show()
