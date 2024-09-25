import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def computeLimit(func, var, point, direction='right'):
    # func: def function()
    # var: a = 2
    # point: the threshold when the limit is processed
    # direction: left, right, both

    if direction == 'both':
        return sp.limit(func, var, point)
    elif direction == 'left':
        return sp.limit(func, var, point, dir='-')
    elif direction == 'right':
        return sp.limit(func, var, point, dir='+')
    else:
        raise ValueError("Invalid direction. Use 'left', 'right', or 'both'.")
    
#plot the function near the limiting point
def plotFunction(func_expr, var, point, x_range=(-10, 10), limit_value=None):
    #func_expre: SymPy expression of the function
    #x_range : tuple for the range of x values 
    #limit_value : the value of the limit, if known 

    # convert sympty function to numpy function for matplotlib readability
    convertSympyToNumpy = sp.lambdify(var, func_expr, 'numpy')
    # generate x values
    x_values = np.linspace(x_range[0], x_range[1], 400)
    #generate y values using lambdified function
    y_values = convertSympyToNumpy(x_values)

    #plot the function
    plt.plot(x_values, y_values, label=f'Function')
    #mark the limit point
    plt.axvline(point, color='red', linestyle='--', label=f'Limit at x = {point}')

    if limit_value is not None:
        plt.scatter(point, limit_value, color='green', zorder=5, label=f'Limit value = {limit_value}')

    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.title(f'Point limit plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

x = sp.symbols('x')
func = (x**2 - 1) / (x - 1)

limit_at_5 = computeLimit(func, x, 5)
print(f"limit of the function as x -> 5: {limit_at_5}")

plotFunction(func, x, 1, x_range=(-5, 10), limit_value=limit_at_5)