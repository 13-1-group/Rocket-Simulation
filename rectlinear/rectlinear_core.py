import matplotlib.pyplot as plt
import numpy as np


def cone(x, z):
    sqrt_y = []
    for x_i in x:
        temp = (1 - 2 * z) * (1 - z) - np.power(x_i, 2) * (1 - 2 * z) / (1 - z)
        if temp < 0:
            x = x[x != x_i]
            continue
        else:
            sqrt_y.append(temp)
    sqrt_y = np.sqrt(sqrt_y)
    # if z > 0.5:
    #     a, b = np.sqrt(1 - 2 * z), np.sqrt(1 - z)
    #     if a > b:
    #         a, b = b, a
    #     e = np.sqrt(1 - b * b / (a * a))
    # elif np.isclose(z, 0.5):
    #     e = 1
    # else:
    #     a, b = np.sqrt(1 - z), np.sqrt(1 - 2 * z)
    #     if a > b:
    #         a, b = b, a
    #     e = np.sqrt(1 + b * b / (a * a))
    return sqrt_y, -sqrt_y, x


z = 0.4
x = np.linspace(-10, 10, 10000)
con = cone(x, z)
plt.grid()
plt.scatter(con[2], con[0], c=con[2], s=0.1)
plt.scatter(con[2], con[1], c=con[2], s=0.1)
plt.show()
