# Problem3: Given a matrix p of m × n integers (non-negative) representing the minimum number of
# trees that must be planted on each plot and an integer h (positive), find the bounding
# indices of a square area where only up to k enclosed plots can have a minimum tree
# requirement of less than h.

# Task7: Design a Θ(mnk) time Dynamic Programming algorithm for solving Problem3
# Task7A: Give a recursive implementation of Alg7 using Memoization.

from run_helper import fetch_input_p3


def find_square_area(m, n, h, p, k):
    memo = [[None] * (n + 1) for _ in range(m + 1)]
    maximum_size = 0
    x1, y1, x2, y2 = -1, -1, -1, -1

    def helper(i, j):
        nonlocal maximum_size, x1, y1, x2, y2

        if memo[i][j] is not None:
            return memo[i][j]

        if i <= 0 or j <= 0:
            memo[i][j] = 0
            return memo[i][j]

        temp = 0
        if p[i-1][j-1] < h:
            temp = 1

        memo[i][j] = helper(i - 1, j) + helper(i, j - 1) - helper(i - 1, j - 1) + temp

        x = maximum_size
        if i - x - 1 >= 0 and j - x - 1 >= 0:
            ans = memo[i][j] + helper(i - x - 1, j - x - 1) - helper(i - x - 1, j) - helper(i, j - x - 1)

            if ans <= k and x + 1 > maximum_size:
                maximum_size = x + 1
                x1, y1 = i - x, j - x
                x2, y2 = i, j

        return memo[i][j]

    helper(m, n)
    return x1, y1, x2, y2


m, n, h, p, k = fetch_input_p3()
x1, y1, x2, y2 = find_square_area(m, n, h, p, k)
print(x1, y1, x2, y2)


