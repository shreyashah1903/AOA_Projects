# Problem1: Given a matrix p of m ×n integers (non-negative) representing the minimum number of
# trees that must be planted on each plot and an integer h (positive), find the bounding
# indices of a square area where each plot enclosed requires a minimum of h trees to be
# planted.

# Task1: Design a Θ(m^3*n^3) time Brute Force algorithm for solving Problem1.
# TODO: Need to find an algo this is similar to Task 2.

from run_helper import fetch_input


def find_square_area(m, n, h, matrix):
    x1, y1, x2, y2 = -1, -1, -1, -1
    maximum_size = 0
    for square_size in range(1, min(m, n) + 1):
        for i in range(0, m - square_size + 1):
            for j in range(0, n - square_size + 1):
                for x in range(i, i + square_size):
                    for y in range(j, j + square_size):
                        valid_area = True
                        for row in range(i, i + square_size):
                            for col in range(j, j + square_size):
                                if matrix[row][col] < h:
                                    valid_area = False
                                    break
                            if not valid_area:
                                break

                        if valid_area and square_size > maximum_size:
                            maximum_size = square_size
                            x1, y1, x2, y2 = i, j, i + square_size - 1, j + square_size - 1
    return x1, y1, x2, y2


m, n, h, p = fetch_input()
x1, y1, x2, y2 = find_square_area(m, n, h, p)
print(x1, y1, x2, y2)
