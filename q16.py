# Write a Python script to create a simple line plot of the function y=x2 and save it in PNG, PDF, and SVG formats. What is the explosion effect on a pie chart?

import numpy as np
import matplotlib.pyplot as plt
# Create data
# x = np.linspace(-10, 10, 100) # 100 points from -10 to 10
x =[1,2,3,4,9,5,6,7]
y = [i ** 2 for i in x]
# y = x ** 2 # y = x squared
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

# What is the explosion effect of pie chart???
# 1. The explosion effect in a pie chart is used to highlight or emphasize a particular slice
# 2. It visually seperated one or more slives from the rest of the chart.
# 3. This seperation draws the viewr's attention to specific data.
# 4. It helps in comparing important segemnets clearly.
# 5. The exploded slice usually represents a key value or important information
# 6. The effect improves the visual appeal and readability of the chart.
# 7. It can be used to show focus on highest or lowest percentage data.
# 8. In short, the explosion effect makes selected slices stand out for emphasis or clarity