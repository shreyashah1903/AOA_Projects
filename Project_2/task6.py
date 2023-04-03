# Problem3: Given a matrix p of m × n integers (non-negative) representing the minimum number of
# trees that must be planted on each plot and an integer h (positive), find the bounding
# indices of a square area where only up to k enclosed plots can have a minimum tree
# requirement of less than h.

# Task6: Design a Θ(m3n3) time Brute Force algorithm for solving Problem3.

from run_helper import fetch_input_p3


def find_square_area(m, n, h, matrix, k):
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

                    if count <= k and size > maximum_size:
                        maximum_size = size
                        # print(i, j, s, t, small_count)
                        x1,y1 = i + 1, j + 1
                        x2,y2 = s + 1, t + 1
    return x1, y1, x2, y2


m, n, h, p, k = fetch_input_p3()
X1, Y1, X2, Y2 = find_square_area(m, n, h, p, k)
print(X1, Y1, X2, Y2)