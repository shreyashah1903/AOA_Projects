# Problem2: Given a matrix p of m × n integers (non-negative) representing the minimum number of trees
# that must be planted on each plot and an integer h (positive), find the bounding indices of a square area
# where all but the corner plots enclosed requires a minimum of h trees to be planted.
# The corner plots can have any number of trees required.

# Task5: Design a Θ(mn) time Dynamic Programming algorithm for solving Problem2.
# Task 5A: Give a recursive implementation of Alg5 using Memoization.
from run_helper import fetch_input


def find_square_area(m, n, h, p):
    memo = [[None] * n for _ in range(m)]
    x1, y1, x2, y2 = -1, -1, -1, -1

    def helper(i, j):
        if i < 0 or j < 0:
            return 0

        if memo[i][j] is not None:
            return memo[i][j]

        if p[i][j] < h:
            memo[i][j] = 0
            return 0

        memo[i][j] = min(helper(i - 1, j), helper(i, j - 1), helper(i - 1, j - 1)) + 1
        return memo[i][j]

    maximum_size = 0
    for i in range(m):
        for j in range(n):
            square_size = helper(i, j)
            if square_size > maximum_size:
                maximum_size = square_size
                x1 = i - maximum_size + 1
                y1 = j - maximum_size + 1
                x2 = i
                y2 = j

    return x1, y1, x2, y2


m, n, h, p = fetch_input()
x1, y1, x2, y2 = find_square_area(m, n, h, p)
print(x1, y1, x2, y2)
