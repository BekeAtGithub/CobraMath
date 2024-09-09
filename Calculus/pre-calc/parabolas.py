import numpy as np
import matplotlib.pyplot as plt

def plotParabola(a, h, k, x_range=(-10, 10), parabola_type='vertical'):
# U vertical lines: y = a(x - h)^2 + k
# U horizont lines: x = a(y - k)^2 + h
# a = coefficient - width and direction
# h = x-coordinate of the vertex 
# k = y-coordinate of the vertex
# x_range = tuple for the range of x values 

    x_values = np.linspace(x_range[0], x_range[1], 400)

    if parabola_type == 'vertical':
        y_values = a * (x_values - h) ** 2 + k 
        plt.plot(x_values, y_values, label=f'Parabola: y = {a}(x - {h})^2 + {k}')
        plt.xlabel('x')
        plt.ylabel('y')
    elif parabola_type == 'horizonal':
        y_values = np.linspace(x_range[0], x_range[1], 400)
        x_values = a * (y_values - k) ** 2 + h
        plt.plot(x_values, y_values, label=f'Parabola: x = {a}(y - {k}^2 + {h})')
    else:
        raise ValueError("invalid type, must be vertical or horizontal")

    plt.scatter(h, k, color='red', zorder=5, label=f'Vertex ({h}, {k})')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.title(f'{parabola_type} Parabola')
    plt.show()

a = 3
h = 1
k = 3
plotParabola(a, h, k, x_range=(-10, 10), parabola_type='vertical')