# Problem2: Given a matrix p of m × n integers (non-negative) representing the minimum number of trees
# that must be planted on each plot and an integer h (positive), find the bounding indices of a square area
# where all but the corner plots enclosed requires a minimum of h trees to be planted.
# The corner plots can have any number of trees required.

# Task5: Design a Θ(m*n) time with a dynamic programming algorithm for solving Problem2.
# # Task 5B: Give an iterative BottomUp implementation of Alg5

from run_helper import fetch_input


def find_square_area(m, n, h, matrix):
    x1, y1, x2, y2 = -1, -1, -1, -1
    dp = [[0] * n for _ in range(m)]
    maximum_size = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] >= h:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

                if dp[i][j] > maximum_size:
                    maximum_size = dp[i][j]
                    x1 = i - maximum_size + 1
                    y1 = j - maximum_size + 1
                    x2 = i
                    y2 = j
    return x1, y1, x2, y2


m, n, h, p = fetch_input()
x1, y1, x2, y2 = find_square_area(m, n, h, p)
print(x1, y1, x2, y2)
