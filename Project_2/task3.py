# Problem1: Given a matrix p of m ×n integers (non-negative) representing the minimum number of
# trees that must be planted on each plot and an integer h (positive), find the bounding
# indices of a square area where each plot enclosed requires a minimum of h trees to be
# planted.

# Task1: Design a Θ(m*n) time with a dynamic programming algorithm for solving Problem1.

from run_helper import fetch_input


def find_square_area(m, n, h, matrix):
    x1, y1, x2, y2 = -1, -1, -1, -1
    dp = [[0] * n + 1 for _ in m + 1]
    maximum_size = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i][j] >= h:
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
