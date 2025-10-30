# Write a Python script to create a histogram from a random dataset and save it in PNG, PDF, and SVG formats.
import matplotlib.pyplot as plt
import numpy as np
# Create random dataset (1000 values around mean 50)
data = np.random.normal(loc=50, scale=10, size=1000)
# Plot histogram
plt.hist(data, bins=20)
plt.title("Histogram of Random Data")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.grid(axis='y')
# Save chart
plt.savefig("histogram.png", bbox_inches='tight')
plt.savefig("histogram.pdf", bbox_inches='tight')
plt.savefig("histogram.svg", bbox_inches='tight')
plt.show()