# importing the required module
import matplotlib.pyplot as plt

# [500, 1000, 1500, 2500] Days
# 500, 1000, 1500, 2000, 2500]
# [496, 979, 1466, 1946, 2426] Strategy 1
# [480, 955, 1420, 1890, 2353] Strategy 2
# [498, 975, 1440, 1928, 2402] Strategy 3
# [500, 995, 1485, 1976, 2467] Strategy 4
# [500, 995, 1485, 1976, 2467] Strategy 5

# x axis values
x = [1000, 2000, 3000, 4000, 5000]
# corresponding y axis values
y1 = [496, 979, 1466, 1946, 2426]

# plotting the points
plt.plot(x, y1, label = "Strategy 1")

# corresponding y axis values
y2 = [480, 955, 1420, 1890, 2353]

plt.plot(x, y2, label = "Strategy 2")


# corresponding y axis values
y3 = [498, 975, 1440, 1928, 2402]

plt.plot(x, y3, label = "Strategy 3")


# corresponding y axis values
y4 = [500, 995, 1485, 1976, 2467]

plt.plot(x, y4, label = "Strategy 4")

# naming the x axis
plt.xlabel('Input size(Days)')
# naming the y axis
plt.ylabel('Houses painted')

# giving a title to my graph
plt.title('Experimental study')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()