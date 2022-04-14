import Orbit
import math
from constants import *


class ElepticalOrbit(Orbit.Orbit):

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    """
    Task -1 
    Orbital parameters after some time after start from earth
    """
    def find_parametrs_eleptical_of_orbit(self) -> tuple:
        """
        Finds the position and velocity of the body 
        some time after the launch in orbit
        """
        pass

    def find_n(self) -> float:
        """
        Find average angular velocity
        :param:
            m1 - mass one of a body
            m2 - mass one of a body
        """
        u = G * (self.m1 + self.m2)
        return math.sqrt(u) * self.a ** (-3 / 2)

    def find_M(self, n: float, t: float, tau: float) -> float:
        """
        Passed corner
        """
        return n * (t - tau)

    def find_E(self, n: float, t: float, tau: float) -> float:
        """
        Find E - НЕОБХОДИМО ПРОВЕРИТЬ
        """
        M = self.find_n()
        return M / (1 - self.e)

    def find_r(self):
        return self.a * (1 - self.e * math.cos(find_E()))

    # ---------------------------------------------------------

    """
    Task -2
    
    """

# a = ElepticalOrbit(3, 4, orbit_type=OrbitTypes.ELLIPTICAL)
# print(a.find_n(4, 5))

# print( math.sqrt(4))