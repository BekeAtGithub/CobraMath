import numpy as np
import matplotlib.pyplot as plt

def plotEllipse(a, b, h, k, angle=0, num_points=400):
# ellipse plotting
#(x - h)^2 / a^2 + (y - k)^2 / b^2 = 1

# a = horizontal width
# b = vertical width
# h = x-coordinate of the vertex 
# k = y-coordinate of the vertex
# angle: Rotation of the ellipse in degrees ( 0 = no rotation )
# num_points: plot the ellipse (400)

    #parametric equations for the ellipse
    t = np.linspace(0, 2 * np.pi, num_points)
    x = a * np.cos(t)
    y = b * np.sin(t)

    #rotation matrix
    angle_radian = np.radians(angle)
    x_rotated = x * np.cos(angle_radian) - y * np.sin(angle_radian)
    y_rotated = x * np.sin(angle_radian) + y * np.cos(angle_radian)

    x_shift = x_rotated + h
    y_shift = y_rotated + k

    plt.plot(x_shift, y_shift, label=f'{h},{a},{k},{b}')

    plt.scatter(h, k, color='red', zorder=5, label=f'Vertex ({h}, {k})')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.title(f'Ellipse')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

a = 3
b = 2
h = -0.04
k = -0.05
angle = 45
plotEllipse(a, b, h, k, angle=angle)