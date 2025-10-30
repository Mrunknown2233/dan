# Write a Python script to create a scatter plot for two variables, x and y, and save it as a PNG, PDF, and SVG file
import matplotlib.pyplot as plt
import numpy as np
# Create data
x = np.random.randint(10, 100, 20) # 20 random x-values
y = np.random.randint(10, 100, 20) # 20 random y-values
# Plot
plt.scatter(x, y)
plt.title("Scatter Plot of X vs Y")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
# Save chart
plt.savefig("scatter_plot.png", bbox_inches='tight')
plt.savefig("scatter_plot.pdf", bbox_inches='tight')
plt.savefig("scatter_plot.svg", bbox_inches='tight')
plt.show()