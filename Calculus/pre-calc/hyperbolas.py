import numpy as np
import matplotlib.pyplot as plt

def plotHyperbola(a, b, h, k, x_range=(-10, 10), hyperbola_type='horizontal'):
# hyperbola plotting
#horizontal : (x - h)^2 / a^2 - (y - k)^2 / b^2 = 1
# vertical  : (y - k)^2 / b^2 - (x - h)^2 / a^2 = 1

# a = horizontal width
# b = vertical width

# h = x-coordinate of the vertex 
# k = y-coordinate of the vertex

# x_range = tuple for the range of x values 

    x_values = np.linspace(x_range[0], x_range[1], 400)

    if hyperbola_type == 'horizontal':
        # equation: (x - h)^2 / a^2 - (y - k)^2 / b^2 = 1
        pos_y_value = k + b * np.sqrt(((x_values - h) ** 2 / a ** 2) - 1)
        neg_y_value = k - b * np.sqrt(((x_values - h) ** 2 / a ** 2) - 1)
    elif hyperbola_type == 'vertical':
        # equation: (y - k)^2 / b^2 - (x - h)^2 / a^2 = 1
        pos_x_value = h + a * np.sqrt(((x_values - h) ** 2 / a ** 2) - 1)
        neg_x_value = h - a * np.sqrt(((x_values - h) ** 2 / a ** 2) - 1)
    else:
        raise ValueError("Invalid type: choose horiztonal or vertical")

    plt.scatter(h, k, color='red', zorder=5, label=f'Vertex ({h}, {k})')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.title(f'{hyperbola_type} Parabola')
    plt.show()

a = 3
b = 2
h = -0.04
k = -0.05
plotHyperbola(a, b, h, k, x_range=(-10, 10), hyperbola_type='vertical')