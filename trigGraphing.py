import math
import matplotlib.pyplot as plt

def graphing_trigonometric_functions():
    # Generate x values from 0 to 2π with step 0.1
    xValues = [x * 0.1 for x in range(0, 63)] #creates graph range
    sinValues = [math.sin(x) for x in xValues]
    cosValues = [math.cos(x) for x in xValues]
    tanValues = [math.tan(x) for x in xValues]

    # Plotting the functions
    plt.figure(figsize=(10, 6))

    plt.plot(xValues, sinValues, label='sin(x)', color='blue')
    plt.plot(xValues, cosValues, label='cos(x)', color='red')
    plt.plot(xValues, tanValues, label='tan(x)', color='green')

    # Adding labels and title
    plt.xlabel('Radians')
    plt.ylabel('Function value')
    plt.title('Trigonometric Functions')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.ylim(-2, 2)  # Limit the y-axis for better visualization of tan(x)
    plt.grid(True)
    plt.legend()

    # Display the plot
    plt.show()

# Call the function to display the plot
graphing_trigonometric_functions()
