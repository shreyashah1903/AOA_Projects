# Problem1: Given a matrix p of m ×n integers (non-negative) representing the minimum number of
# trees that must be planted on each plot and an integer h (positive), find the bounding
# indices of a square area where each plot enclosed requires a minimum of h trees to be
# planted.

# Task1: Design a Θ(m^3*n^3) time Brute Force algorithm for solving Problem1.

from run_helper import fetch_input


def find_square_area(m, n, h, matrix):
    x1, y1, x2, y2 = -1, -1, -1, -1
    maximum_size = 0
    for i in range(m):
        for j in range(n):
            for s in range(i, m):
                for t in range(j, n):
                    count = 0
                    # Check if the formed matrix is a square or not
                    if s + 1 - i != t + 1 - j:
                        continue
                    size = s + 1 - i
                    for x in range(i, s + 1):
                        for y in range(j, t + 1):
                            if matrix[x][y] < h:
                                count += 1

                    if count == 0 and size > maximum_size:
                        maximum_size = size
                        # print(i, j, s, t, small_count)
                        x1, y1 = i + 1, j + 1
                        x2, y2 = s + 1, t + 1
    return x1, y1, x2, y2


m, n, h, p = fetch_input()
x1, y1, x2, y2 = find_square_area(m, n, h, p)
print(x1, y1, x2, y2)
