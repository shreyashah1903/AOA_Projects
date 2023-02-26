from task1 import *
from task2 import *
from task3 import *
from task4 import *
from task5_bonus import *

def test_strategies():
    files = ["test/file2.txt"]
    for filename in files:
        with open(filename, "r") as file:
            lines = file.readlines()
            case = 1

            for i in range(len(lines)):
                index = 0
                # check if line is a test case header
                if lines[i].startswith("# Test"):

                    # extract values for test case
                    n, m = map(int, lines[i + 1].split())

                    # initialize 2D array
                    data = [[0] * 2 for _ in range(m)]

                    # loop through rows and add to 2D array
                    for j in range(i + 2, i + 2 + m):
                        row = list(map(int, lines[j].split()))
                        data[index][0] = row[0]
                        data[index][1] = row[1]
                        index += 1

                    print("Test case", case)
                    print("days =", n)
                    print("houses =", m)
                    print("House availability =", data)

                    print("\nStrategy 1")
                    painted_houses = count_houses_strategy1(data, n, m)
                    print("Num of houses painted:", len(painted_houses))
                    for j in range(len(painted_houses)):
                        start, end, day, index = painted_houses[j]
                        print("Day {}, house {} painted with schedule {} {}".format(day, index, start, end))

                    print("\nStrategy 2")
                    painted_houses = count_houses_strategy2(data, n, m)
                    print("Num of houses painted:", len(painted_houses))
                    for j in range(len(painted_houses)):
                        start, end, day, index = painted_houses[j]
                        print("Day {}, house {} painted with schedule {} {}".format(day, index, start, end))

                    print("\nStrategy 3")
                    painted_houses = count_houses_strategy3(data, n, m)
                    print("Num of houses painted:", len(painted_houses))
                    for j in range(len(painted_houses)):
                        start, end, day, index = painted_houses[j]
                        print("Day {}, house {} painted with schedule {} {}".format(day, index, start, end))

                    print("\nStrategy 4")
                    painted_houses = count_houses_strategy4(data, n, m)
                    print("Num of houses painted:", len(painted_houses))

                    for j in range(len(painted_houses)):
                        start, end, day, index = painted_houses[j]
                        print("Day {}, house {} painted with schedule {} {}".format(day, index, start, end))

                    print("\nStrategy 5 (Bonus)")
                    painted_houses = count_houses_bonus_strategy(data, n, m)
                    print("Num of houses painted:", len(painted_houses))

                    for j in range(len(painted_houses)):
                        start, end, day, index = painted_houses[j]
                        print("Day {}, house {} painted with schedule {} {}".format(day, index, start, end))

                    print()

                    case += 1
                    # # move to next test case
                    i = i + m + 2

                else:
                    # move to next line
                    i += 1


if __name__ == '__main__':
    test_strategies()
