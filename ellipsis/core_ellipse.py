import numpy as np
from matplotlib import pyplot as plt
from math import pi

class EllipsePlot():
    def __init__(self, a, b):
        """
        Paramenets:
            a - semi-major axis
            b - semi-minor axis
        """
        self.a = a
        self.b = b

    def plot_ellipsys(self) -> float:
        """
        Returned:
            draws given `a` and `b` an ellipse
        """
        t = np.linspace(0, 2 * pi, 100)
        Ell = np.array([self.a * np.cos(t), self.b * np.sin(t)])  
        plt.plot( Ell[0, :], Ell[1, :] )   
        plt.grid(color='lightgray', linestyle='--')
        plt.show()