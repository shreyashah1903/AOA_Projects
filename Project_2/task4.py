# Problem 2 : Given a matrix p of m × n integers (non-negative) representing the minimum number of
# trees that must be planted on each plot and an integer h (positive), find the bounding
# indices of a square area where all but the corner plots enclosed requires a minimum of h
# trees to be planted. The corner plots can have any number of trees required.
import sys

# Task 4 : Design a Θ(m*n^2) time Dynamic Programming algorithm for solving Problem2.

from run_helper import fetch_input


def find_square_area(m, n, h, matrix):
    # nonlocal maximum_size, x1, y1, x2, y2
    x1, y1, x2, y2 = -1, -1, -1, -1
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    maximum_size = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # print(i, j)
            if matrix[i - 1][j - 1] < h:
                temp = 1
            else:
                temp = 0
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + temp

            for x in range(0, min(i, j)):
                ans = dp[i][j] + dp[i - x-1][j - x-1] - dp[i - x-1][j] - dp[i][j - x-1]
                # print(i-x, j-x, x+1, maximum_size)
                if ans <= 4:
                    corner_points = [(i, j), (i - x, j - x), (i - x, j), (i, j - x)]
                    count = 0
                    for a, b in corner_points:
                        if matrix[a - 1][b - 1] < h:
                            count += 1
                    if count == ans and x+1 > maximum_size:
                        maximum_size = x + 1
                        x1 = i - x
                        y1 = j - x
                        x2 = i
                        y2 = j
    return x1, y1, x2, y2


m, n, h, p = fetch_input()
x1, y1, x2, y2 = find_square_area(m, n, h, p)
print(x1, y1, x2, y2)