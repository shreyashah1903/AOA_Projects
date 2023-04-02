def fetch_input():
    m, n, h = map(int, input().split())
    p = []
    for i in range(m):
        row = list(map(int, input().split()))
        if len(row) != n:
            print("Error: Each row should have {} integers.".format(n))
            return None
        p.append(row)
    return m, n, h, p


def fetch_input_p3():
    m, n, h, k = map(int, input().split())
    p = []
    for i in range(m):
        row = list(map(int, input().split()))
        if len(row) != n:
            print("Error: Each row should have {} integers.".format(n))
            return None
        p.append(row)
    return m, n, h, p, k
