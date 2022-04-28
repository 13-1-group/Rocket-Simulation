from matplotlib.animation import writers
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

class E():
    def __init__(self, a, eccentricity) -> None:
        self.a = a 
        self.eccentricity = eccentricity
        self.b = None
        

    def solar_system(self, earth, earth_o, x1, y1):
        for i in range(361):
            earth.set_data(x1[i], y1[i])
            earth_o.set_data(x1[:i], y1[:i])

        return earth, earth_o

    def visualuze(self):
        self.b = self.a * np.sqrt(1-self.eccentricity**2)

        fig = plt.figure()
        ax = plt.axes(xlim=(-10.2, 10.2), ylim=(-10.2, 10.2))

        earth, = ax.plot([], [],marker='o',markersize= 4,markerfacecolor='dodgerblue',label='Earth')
        earth_o, = ax.plot([],[],color='y',lw=1.5)

        t = np.linspace(0, 2 * np.pi, 361)
        x1 = self.a * np.cos(t) - self.a * self.eccentricity
        y1 = self.b * np.sin(t)


        
        anim=animation.FuncAnimation(fig, self.solar_system(earth, earth_o, x1, y1), frames = len(t), interval=25, blit=True, repeat =True)
        fig.patch.set_facecolor('k')
        fig.tight_layout()
        plt.plot(self.a * self.eccentricity,0,'ro',markersize=6.5, label='Sun')
        plt.axis(False)
        plt.legend()
        plt.show()


