# Problem3: Given a matrix p of m × n integers (non-negative) representing the minimum number of
# trees that must be planted on each plot and an integer h (positive), find the bounding
# indices of a square area where only up to k enclosed plots can have a minimum tree
# requirement of less than h.

# Task7: Design a Θ(mnk) time Dynamic Programming algorithm for solving Problem3
# Task 7B: Give an iterative BottomUp implementation of Alg7.

from run_helper import fetch_input_p3


def find_square_area(m, n, h, matrix, k):
    x1, y1, x2, y2 = -1, -1, -1, -1
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    maximum_size = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] < h:
                temp = 1
            else:
                temp = 0
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + temp
            x = maximum_size
            if i - x - 1 >= 0 and j - x - 1 >= 0:
                ans = dp[i][j] + dp[i - x-1][j - x-1] - dp[i - x-1][j] - dp[i][j - x-1]
                if ans <= k and x+1 > maximum_size:
                    maximum_size = x+1
                    x1 = i - x
                    y1 = j - x
                    x2 = i
                    y2 = j

    return x1, y1, x2, y2


m, n, h, p, k = fetch_input_p3()
x1, y1, x2, y2 = find_square_area(m, n, h, p, k)
print(x1, y1, x2, y2)
