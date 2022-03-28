import numpy as np
from math import pi
from constants import OrbitTypes


class Orbit:
    def __init__(self, a, b, x=np.linspace(-2 * pi, 2 * pi, 100), orbit_type=OrbitTypes.PARABOLIC):
        """
        :param:
            a - semi-major axis
            b - semi-minor axis
            x - numpy array of x values
            orbit_type - type of orbit
        """
        self.a = a
        self.b = b
        self.x = x
        self.orbit_type = orbit_type

    def get_coordinates(self):
        """
            generates x,y arrays
            y generation depending on orbit_type
        :return:
            X array
            Y array
        """
        if self.orbit_type == OrbitTypes.HYPERBOLIC:
            return self.x, (self.x ** 2 * self.b ** 2) / self.a ** 2 ** 0.5
