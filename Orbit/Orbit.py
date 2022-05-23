import numpy as np
from constants import OrbitType
import Exceptions.IncorrectOrbitException as IncorrectOrbitException
import matplotlib.pyplot as plt

import numpy as np
from constants import AstronomicalConstants


class OrbitFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_orbit(v, r):
        G = 6.667e-11
        ME = 5.97e+24
        h = np.cross(v, r, axis=0)
        h_norm = np.linalg.norm(h)
        r_norm = np.linalg.norm(r)
        MU = ME * G
        p = h_norm * h_norm / MU
        h_v = np.cross(h, v)
        e = np.linalg.norm(h_v / MU - r / r_norm)
        if np.isnan(p):
            raise ArithmeticError('Focal parameter is nan')
        elif np.isnan(e):
            raise ArithmeticError('Eccentricity is nan')
        else:
            return Orbit(e, p)


class Orbit:
    def __init__(self, e, p):
        """
        :param:
            a - semi-major axis
            b - semi-minor axis
            x - numpy array of x values
            orbit_type - type of orbit
        """
        self.e = e
        self.p = p

    def get_type(self) -> OrbitType:
        if self.e == 0:
            return OrbitType.BARYCENTRIC
        elif 0 < self.e < 1:
            return OrbitType.ELLIPTICAL
        elif self.e == 1:
            return OrbitType.PARABOLIC
        elif 1 < self.e < float('inf'):
            return OrbitType.HYPERBOLIC
        elif self.e == float('inf'):
            return OrbitType.RECTILINEAR
        elif self.e <= 0:
            raise Exception('Incorrect orbit type! Eccentricity is lower than one')

    def get_polar_coordinates(self, theta: np.ndarray):
        """
            generates x,y arrays
            y generation depending on orbit_type
        :return:
            X array
            Y array
        """
        r = np.full(theta.shape, self.p) / (np.full(theta.shape, 1) + np.full(theta.shape, self.e) * np.cos(theta))
        return r, theta

    @staticmethod
    def polar_to_cartesian(r, theta):
        x, y = [], []
        for r_i, theta_i in zip(r, theta):
            x.append(r_i * np.cos(theta_i))
            y.append(r_i * np.sin(theta_i))
        return x, y


if __name__ == '__main__':
    o = OrbitFactory.get_orbit(np.array([8, 2, 3]), np.array([3, 2, 3]))
    theta = np.linspace(0, 2 * np.pi)
    r, theta = o.get_polar_coordinates(theta)
    coords = Orbit.polar_to_cartesian(r, theta)
    for i in coords:
        print(i)
    plt.plot(coords)
    # plt.plot(o.get_trajectory()[1])
    plt.show()
