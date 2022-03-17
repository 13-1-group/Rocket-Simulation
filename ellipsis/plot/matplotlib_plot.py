import numpy as np
from matplotlib import pyplot as plt
from math import pi, cos, sin

def plot_ellipsys(u : float, v, a, b) -> float:
    """
    Paramenets

    """
    t_rot=pi/4 

    t = np.linspace(0, 2*pi, 100)
    Ell = np.array([a*np.cos(t), b*np.sin(t)])  

    R_rot = np.array([[cos(t_rot), -sin(t_rot)],[sin(t_rot) , cos(t_rot)]])  

    Ell_rot = np.zeros((2,Ell.shape[1]))
    for i in range(Ell.shape[1]):
        Ell_rot[:,i] = np.dot(R_rot, Ell[:,i])

    plt.plot( u+Ell[0,:] , v+Ell[1,:] )   
    plt.plot( u+Ell_rot[0,:] , v+Ell_rot[1,:],'darkorange')
    plt.grid(color='lightgray', linestyle='--')
    plt.show()