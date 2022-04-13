from enum import Enum


G = 6.67 * 10 ** (-11)

class OrbitTypes(Enum):
    ELLIPTICAL = 'Elliptical'
    PARABOLIC = 'Parabolic'
    HYPERBOLIC = 'Hyperbolic'
    RECTILINEAR = 'Rectilinear'
    BARYCENTRIC = 'Barycentric'

