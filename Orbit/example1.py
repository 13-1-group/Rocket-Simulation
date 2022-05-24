from matplotlib.animation import writers
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

BOUNDS_X = (-20.2, 20.2)
BOUNDS_Y = (-20.2, 20.2)
# Semimajor and semiminor distances of planet's and comet's orbit are in AU
p1_p = 4
# p1_p =

fig = plt.figure()
ax = plt.axes(xlim=BOUNDS_X, ylim=BOUNDS_Y)

rocket, = ax.plot([], [], marker='o', markersize=4, markerfacecolor='red', label='Rocket')
rocket_o, = ax.plot([], [], color='w', lw=1.5)

t = np.linspace(-np.pi/2+0.0001, np.pi/2-0.0001, 361)[::-1]

x1 = p1_p / (1 - np.sin(t)) * np.cos(t)
y1 = p1_p / (1 - np.sin(t)) * np.sin(t)
x1 = np.array(list(-1 * x1) + list(x1[::-1]))
y1 = np.array(list(y1) + list(y1[::-1]))

def solar_system(i):
    rocket.set_data(x1[i], y1[i])
    rocket_o.set_data(x1[:i], y1[:i])
    return rocket, rocket_o


anim = animation.FuncAnimation(fig, solar_system, frames=2*len(t), interval=25, blit=True, repeat=True)
fig.patch.set_facecolor('k')
fig.tight_layout()
plt.plot(0, p1_p / (1 - np.sin(3*np.pi / 2)) * np.sin(3 * np.pi / 2) + p1_p / 2, 'yo', markersize=6.5, label='Moon')
plt.axis(False)
plt.legend()
plt.show()
