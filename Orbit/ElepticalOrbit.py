import Orbit
import math
from constants import *


class ElepticalOrbit(Orbit.Orbit):
    
    def find_parametrs_eleptical_of_orbit(self) -> tuple:
        """
        Finds the position and velocity of the body 
        some time after the launch in orbit
        """
        pass

    def find_n(self, m1: float, m2: float) -> float:
        """
        Find average angular velocity
        :param:
            m1 - mass one of a body
            m2 - mass one of a body
        """
        u = G * (m1 + m2)
        return math.sqrt(u) * self.a ** (-3 / 2)

# a = ElepticalOrbit(3, 4, orbit_type=OrbitTypes.ELLIPTICAL)
# print(a.find_n(4, 5))

# print( math.sqrt(4))