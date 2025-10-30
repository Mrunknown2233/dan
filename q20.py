# Write a Python script to create a pie chart that shows the distribution of market share among 5 companies, and save it as PNG, PDF, and SVG files.

import matplotlib.pyplot as plt
# Data
companies = ['A', 'B', 'C', 'D', 'E']
market_share = [25, 20, 30, 15, 10]
# Identify largest share to highlight
largest_index = market_share.index(max(market_share))
explode = [0.1 if i == largest_index else 0 for i in range(len(market_share))]
# Plot pie chart
plt.pie(market_share, labels=companies, autopct='%1.1f%%', startangle=90,
explode=explode)
plt.title("Market Share of 5 Companies")
plt.axis('equal') # Make circle round
# Save chart
plt.savefig("market_share.png", bbox_inches='tight')
plt.savefig("market_share.pdf", bbox_inches='tight')
plt.savefig("market_share.svg", bbox_inches='tight')
plt.show()