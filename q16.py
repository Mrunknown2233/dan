# Write a Python script to create a simple line plot of the function y=x2 and save it in PNG, PDF, and SVG formats. What is the explosion effect on a pie chart?

import numpy as np
import matplotlib.pyplot as plt
# Create data
x = np.linspace(-10, 10, 100) # 100 points from -10 to 10
y = x ** 2 # y = x squared
# Plot
plt.plot(x, y)
plt.title("Graph of y = x²")
plt.xlabel("x values")
plt.ylabel("y = x²")
plt.grid(True)
# Save in multiple formats
plt.savefig("y_equals_x2.png", bbox_inches='tight')
plt.savefig("y_equals_x2.pdf", bbox_inches='tight')
plt.savefig("y_equals_x2.svg", bbox_inches='tight')
plt.show()
