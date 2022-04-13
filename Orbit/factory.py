from orbit.constants import OrbitTypes
from orbit.otypes import(
        elliptical, 
        parabolic,
        hyperbolic,
        barycentric,
        rectilinear
)


class Factory:
    def build(self, type):
        if type.o_type == OrbitTypes.ELLIPTICAL.value:
            print(f'you are select a `{str(type.o_type)}` orbit')
            return elliptical.E()

        elif type.o_type == OrbitTypes.PARABOLIC.value:
            print(f'you are select a `{str(type.o_type)}` orbit')
            obj = parabolic.P()
            print(obj.method1())
            return parabolic.P()

        elif self.o_type.o_type == OrbitTypes.HYPERBOLIC.value:
            print(f'you are select a `{str(type.o_type)}` orbit')
            return hyperbolic.H()

        elif type.o_type == OrbitTypes.RECTILINEAR.value:
            print(f'you are select a `{str(type.o_type)}` orbit')
            return  rectilinear.R()

        elif type.o_type == OrbitTypes.BARYCENTRIC.value:
            print(f'you are select a `{str(type.o_type)}` orbit')
            return barycentric.B()
        else:
            raise ValueError(type.o_type)


class Orbit:
    def __init__(self, o_type=None):
        self.o_type = o_type



    

