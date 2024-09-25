import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#defining or computing the end behavior symbolically to infinity 
def endBehavior(func, var):
    # func: def function()
    # var: a = 2
    limit_at_pos = sp.limit(func, var, sp.oo)
    limit_at_neg = sp.limit(func, var, -sp.oo)
    return limit_at_pos, limit_at_neg

#function to plot and visualize end behavior 
def plotEndBehavior(func_expr, var, x_range=(-10, 10)):
    #func_expre: SymPy expression of the function
    #x_range : tuple for the range of x values 

    # convert sympty function to numpy function for matplotlib readability
    convertSympyToNumpy = sp.lambdify(var, func_expr, 'numpy')
    # generate x values
    x_values = np.linspace(x_range[0], x_range[1], 400)
    #generate y values using lambdified function
    y_values = convertSympyToNumpy(x_values)

    plt.plot(x_values, y_values, label=f'Function {sp.pretty(func_expr)}')

    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(True)
    plt.title(f'Point limit plot')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

x = sp.symbols('x')
func = (3*x**3 - 2*x + 1) / (x - 1)

#compute the end behavior as x approached infinity and negative infinity
limit_at_pos, limit_at_neg = endBehavior(func, x)
print(f"End behavior as x -> infinity and beyond: {limit_at_pos}")
print(f"End behavior as x -> negative infinity and beyond: {limit_at_neg}")

#plot function and visualize
plotEndBehavior(func, x, x_range=(-10, 10))