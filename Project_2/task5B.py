# Problem 2 : Given a matrix p of m × n integers (non-negative) representing the minimum number of
# trees that must be planted on each plot and an integer h (positive), find the bounding
# indices of a square area where all but the corner plots enclosed requires a minimum of h
# trees to be planted. The corner plots can have any number of trees required.

# Task 5B: Design a Θ(mn) time Dynamic Programming algorithm using bottom up aaproach for solving Problem2.

from run_helper import fetch_input

def find_square_area(m, n, h, matrix):
    x1, y1, x2, y2 = -1, -1, -1, -1
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    maximum_size = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i-1][j-1] >= h:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

            l = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
            if l + 2 >= maximum_size:
                maximum_size = l + 2
                x1, y1 = i - maximum_size + 1, j - maximum_size + 1
                x2, y2 = i, j

    return x1, y1, x2, y2


m, n, h, p = fetch_input()
x1, y1, x2, y2 = find_square_area(m, n, h, p)
print(x1, y1, x2, y2)