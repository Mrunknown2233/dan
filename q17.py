# Write a Python script to create a bar chart displaying the sales of a product over 6 months and save the plot in PNG, PDF, and SVG formats.
import matplotlib.pyplot as plt
# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 180, 200, 220, 210, 230] # Example values
# Plot
plt.bar(months, sales)
plt.title("Product Sales Over 6 Months")
plt.xlabel("Months")
plt.ylabel("Sales (Units)")
plt.grid(axis='y')
# Save chart
plt.savefig("product_sales.png", bbox_inches='tight')
plt.savefig("product_sales.pdf", bbox_inches='tight')
plt.savefig("product_sales.svg", bbox_inches='tight')
plt.show()