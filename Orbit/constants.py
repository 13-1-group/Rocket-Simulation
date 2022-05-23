from enum import Enum


class OrbitType(Enum):
    ELLIPTICAL = 'Elliptical'
    PARABOLIC = 'Parabolic'
    HYPERBOLIC = 'Hyperbolic'
    RECTILINEAR = 'Rectilinear'
    BARYCENTRIC = 'Barycentric'


class AstronomicalConstants(Enum):
    G = 6.667e-11
    ME = 5.97e+24
