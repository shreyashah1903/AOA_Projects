import random


def generate_testcase(m, n, f):
    available = []
    for i in range(m):
        start_day = random.randint(0, max(n+1-i, 2))
        j = random.randint(5, int(m/8))
        end_day = random.randint(start_day + 1, start_day + f)
        available.append([start_day, min(end_day, n)])
    return available

MAX1 = 100000
ns = [1000, 2000, 3000, 5000]
for index, n in enumerate(ns):
    m = int(n/2)
    f = 6
    a = generate_testcase(m, n, f)
    a.sort(key=lambda x: (x[0], x[1]))
    print("# Testcase", index+1)
    print(n, m)
    for ar in a:
        print(ar[0], ar[1])
    print()
