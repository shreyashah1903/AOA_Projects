# Problem2: Given a matrix p of m × n integers (non-negative) representing the minimum number of trees
# that must be planted on each plot and an integer h (positive), find the bounding indices of a square area
# where all but the corner plots enclosed requires a minimum of h trees to be planted.
# The corner plots can have any number of trees required.

# Task5: Design a Θ(mn) time Dynamic Programming algorithm for solving Problem2.
# Task 5A: Give a recursive implementation of Alg5 using Memoization.
from run_helper import fetch_input


def find_square_area(m, n, h, p):
    memo = [[None] * (n + 1) for _ in range(m + 1)]
    x1, y1, x2, y2 = -1, -1, -1, -1
    maximum_size = 0

    def helper(i, j):
        nonlocal maximum_size, x1, y1, x2, y2

        if i == 0 or j == 0:
            memo[i][j] = 0
            return memo[i][j]

        if memo[i][j] is not None:
            return memo[i][j]

        if p[i - 1][j - 1] < h:
            memo[i][j] = 0
        else:
            memo[i][j] = min(helper(i - 1, j), helper(i, j - 1), helper(i - 1, j - 1)) + 1

        l = min(helper(i - 1, j), helper(i, j - 1), helper(i - 1, j - 1))
        if l + 2 >= maximum_size:
            maximum_size = l + 2
            x1, y1 = i - maximum_size + 1, j - maximum_size + 1
            x2, y2 = i, j

        return memo[i][j]

    helper(m, n)
    return x1, y1, x2, y2


m, n, h, p = fetch_input()
maximum_size = 0
x1, y1, x2, y2 = find_square_area(m, n, h, p)
print(x1, y1, x2, y2)
