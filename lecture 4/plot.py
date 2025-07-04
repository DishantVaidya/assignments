import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*np.pi,100)  # Create an array of 100 points from 0 to 2*pi

y = np.sin(x)  # Calculate the sine of each point

# %matplotlib inline  # This is only needed in Jupyter Notebook, not in regular Python scripts

plt.plot(x, y)  # Plot the sine wave
plt.show() # Display the plot

