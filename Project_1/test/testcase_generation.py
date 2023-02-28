import random


def generate_testcase(m, n, f):
    available = []
    for i in range(m):
        start_day = random.randint(0, max(n+1-i, 2))
        j = random.randint(1, int(m/4))
        end_day = random.randint(start_day + 1, start_day + j)
        available.append([start_day, min(end_day, 10001)])
    return available

# m = 5000
f = 6

MAX1 = 100000
ns = [1000, 2000, 3000, 4000, 5000, 10000]
for index, n in enumerate(ns):
    i = 0
    filename = 'testcases_for_n_' + str(n) + '.txt'
    file = open(filename, 'w')
    for m in [int(n/16), int(n/8), int(n/4), int(n/2), n]:
        a = generate_testcase(m, n, f)
        a.sort(key=lambda x: (x[0], x[1]))
        file.write("# Testcase {}\n".format(str(i+1)))
        file.write("{} {}\n".format(n, m))
        for ar in a:
            file.write("{} {}\n".format(ar[0], ar[1]))
        # file.write("\n")
        i += 1
    file.close()

