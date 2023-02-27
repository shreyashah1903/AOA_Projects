import matplotlib.pyplot as plt
import numpy as np

# Input data
x = [1000, 2000, 3000, 4000, 5000]
y1 = [496, 979, 1466, 1946, 2426]
y2 = [480, 955, 1420, 1890, 2353]
y3 = [498, 975, 1440, 1928, 2402]
y4 = [500, 995, 1485, 1976, 2467]

# Create a figure with a single subplot
fig, ax = plt.subplots()

# Set the bar width
bar_width = 0.1

# Set the positions of the bars on the x-axis
bar_positions1 = np.arange(len(x))
bar_positions2 = [x + bar_width for x in bar_positions1]
bar_positions3 = [x + bar_width * 2 for x in bar_positions1]
bar_positions4 = [x + bar_width * 3 for x in bar_positions1]

# Create the bars
ax.bar(bar_positions1, y1, width=bar_width, label='Strategy 1')
ax.bar(bar_positions2, y2, width=bar_width, label='Strategy 2')
ax.bar(bar_positions3, y3, width=bar_width, label='Strategy 3')
ax.bar(bar_positions4, y4, width=bar_width, label='Strategy 4')

# Add x-axis ticks and labels
plt.xticks([i + bar_width * 1.5 for i in range(len(x))], x)

# Add labels and legend
plt.xlabel('Input size(Days)')
plt.ylabel('Houses painted')
plt.title('Experimental Study')
plt.legend()

# Show the plot
plt.show()
