import time

import numpy as np
from matplotlib import pyplot as plt

from Project_1.test.testcase_generation import generate_testcase
from task1 import *
from task2 import *
from task3 import *
from task4 import *
from task5_bonus import *

N_values = [1000, 2000, 3000, 4000, 5000, 10000]


def test_strategies(isComparative):
    if isComparative: files = ["test/testcases_for_n_" + str(x) + ".txt" for x in N_values]
    else: files = ["test/file1.txt", "test/file2.txt"]
    for index, filename in enumerate(files):
        with open(filename, "r") as file:
            lines = file.readlines()
            case = 1

            ns = []
            ms = []
            s1 = []
            s2 = []
            s3 = []
            s4 = []
            s5 = []

            for i in range(len(lines)):
                index = 0
                # check if line is a test case header
                if lines[i].startswith("# Test"):

                    # extract values for test case
                    n, m = map(int, lines[i + 1].split())

                    # initialize 2D array
                    data = [[0] * 2 for _ in range(m)]

                    # loop through rows and add to 2D array
                    print("{} {} {}".format(file, n, case))
                    for j in range(i + 2, i + 2 + m):
                        row = list(map(int, lines[j].split()))
                        data[index][0] = row[0]
                        data[index][1] = row[1]
                        index += 1

                    print("Test case", case)
                    print("days =", n)
                    print("houses =", m)
                    print("House availability =", data)
                    ns.append(n)
                    ms.append(m)

                    print("\nStrategy 1")
                    painted_houses = count_houses_strategy1(data, n, m)
                    print("Num of houses painted:", len(painted_houses))
                    s1.append(len(painted_houses))
                    for j in range(len(painted_houses)):
                        start, end, day, index = painted_houses[j]
                        # print("Day {}, house {} painted with schedule {} {}".format(day, index, start, end))

                    print("\nStrategy 2")
                    painted_houses = count_houses_strategy2(data, n, m)
                    print("Num of houses painted:", len(painted_houses))
                    s2.append(len(painted_houses))
                    for j in range(len(painted_houses)):
                        start, end, day, index = painted_houses[j]
                        # print("Day {}, house {} painted with schedule {} {}".format(day, index, start, end))

                    print("\nStrategy 3")
                    painted_houses = count_houses_strategy3(data, n, m)
                    print("Num of houses painted:", len(painted_houses))
                    s3.append(len(painted_houses))
                    for j in range(len(painted_houses)):
                        start, end, day, index = painted_houses[j]
                        # print("Day {}, house {} painted with schedule {} {}".format(day, index, start, end))

                    print("\nStrategy 4")
                    painted_houses = count_houses_strategy4(data, n, m)
                    print("Num of houses painted:", len(painted_houses))
                    s4.append(len(painted_houses))
                    for j in range(len(painted_houses)):
                        start, end, day, index = painted_houses[j]
                        # print("Day {}, house {} painted with schedule {} {}".format(day, index, start, end))

                    print("\nStrategy 5 (Bonus)")
                    painted_houses = count_houses_bonus_strategy(data, n, m)
                    print("Num of houses painted:", len(painted_houses))
                    s5.append(len(painted_houses))
                    for j in range(len(painted_houses)):
                        start, end, day, index = painted_houses[j]
                        # print("Day {}, house {} painted with schedule {} {}".format(day, index, start, end))

                    print()

                    case += 1
                    # # move to next test case
                    i = i + m + 2

                else:
                    # move to next line
                    i += 1

            plot_graph1(n, ns, ms, s1, s2, s3, s4, s5)


def plot_graph1(n, ns, ms, s1, s2, s3, s4, s5):
    # Create a figure with a single subplot
    fig, ax = plt.subplots()
    x = ms
    bar_width = 0.1

    # Set the positions of the bars on the x-axis
    bar_positions1 = np.arange(len(x))
    bar_positions2 = [x + bar_width for x in bar_positions1]
    bar_positions3 = [x + bar_width * 2 for x in bar_positions1]
    bar_positions4 = [x + bar_width * 3 for x in bar_positions1]

    # Create the bars
    ax.bar(bar_positions1, s1, width=bar_width, label='Strategy 1')
    ax.bar(bar_positions2, s2, width=bar_width, label='Strategy 2')
    ax.bar(bar_positions3, s3, width=bar_width, label='Strategy 3')
    ax.bar(bar_positions4, s4, width=bar_width, label='Strategy 4')

    # Add x-axis ticks and labels
    plt.xticks([i + bar_width * 1.5 for i in range(len(x))], x)

    # Add x-axis ticks and labels
    plt.xlabel('No of Houses')
    plt.ylabel('Houses painted')
    plt.title('Experimental Study for Number of Days (n = {})'.format(n))
    plt.legend()

    # Show the plot
    plt.show()


def plot_graph(n, ns, ms, s1, s2, s3, s4, s5):
    print("Graph data")
    print(ns)
    print(ms)
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)

    plt.plot(ms, s1, label="Strategy 1")
    plt.plot(ms, s2, label="Strategy 2")
    plt.plot(ms, s3, label="Strategy 3")
    plt.plot(ms, s4, label="Strategy 4")

    # naming the x axis
    plt.xlabel('No of houses')
    # naming the y axis
    plt.ylabel('Houses painted')

    # giving a title to my graph
    plt.title('Experimental study (n={})'.format(n))

    # show a legend on the plot
    plt.legend()

    # function to show the plot
    plt.show()


def comparative_study_bonus():
    for n in [10 ** 6, 10 ** 5, 10 ** 4, 10 ** 3, 10 ** 2]:
        ms = []
        s4 = []
        s5 = []
        for m in [int(n/16), int(n / 8), int(n / 4), int(n / 2)]:
            ms.append(m)
            schedule = generate_testcase(m, n, 6)
            schedule.sort(key=lambda x: (x[0], x[1]))

            # Strategy 5
            start_time = time.time()
            _ = count_houses_bonus_strategy(schedule, n, m)
            end_time = time.time()
            time_taken = end_time - start_time
            s5.append(time_taken)

            # Strategy 4
            start_time = time.time()
            _ = count_houses_strategy4(schedule, n, m)
            end_time = time.time()
            time_taken = end_time - start_time
            s4.append(time_taken)



        plot_graph_running_time(n, ms, s4, s5)


def plot_graph_running_time(n, ms, s4, s5):
    # Create a figure with a single subplot
    fig, ax = plt.subplots()
    x = ms
    bar_width = 0.2

    # Set the positions of the bars on the x-axis
    bar_positions1 = np.arange(len(x))
    bar_positions2 = [x + bar_width for x in bar_positions1]

    # Create the bars
    ax.bar(bar_positions1, s4, width=bar_width, label='Strategy 4 (Theta(n + mlogm)')
    ax.bar(bar_positions2, s5, width=bar_width, label='Strategy 5 (Theta(mlogm))')

    # Add x-axis ticks and labels
    plt.xticks([i + bar_width * 1.5 for i in range(len(x))], x)

    # Add x-axis ticks and labels
    plt.xlabel('No of Houses')
    plt.ylabel('Time taken to run')
    plt.title('Experimental Study for Number of Days (n = {})'.format(n))
    plt.legend()

    # Show the plot
    plt.show()


if __name__ == '__main__':
    test_strategies(True)
    # comparative_study_bonus()
