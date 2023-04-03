# from Project_2 import task5A, task5B, task6, task7A, task7B
import subprocess
import time

import matplotlib.pyplot as plt
import numpy as np

input_dir = 'input'
ip_sizes = [10, 25, 50, 100]
# ip_sizes = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8]

file_list_1 = ['task1', 'task2', 'task3']
file_list_2 = ['task4', 'task5A', 'task5B']
file_list_3 = ['task6', 'task7A', 'task7B']

ext = '.py'


def helper_function(filename, ip_sizes):
    # module_name = filename  # Assumes the file has a .py extension
    # module = __import__(ip_sizes)
    # function_name = module.function.__name__
    # function = get_function(filename)
    print("helper file:", filename)
    times = []
    for sz in ip_sizes:
        print("Size:", sz)
        m, n = sz, int(sz + sz / 100)
        matrix = np.random.randint(20, size=(m, n))
        h, k = 10, 15

        input_bytes = convert_input(m, n, h, k, matrix, filename in file_list_3)
        start_time = time.time()

        process = subprocess.Popen(["python3", filename + ext], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, _ = process.communicate(input=input_bytes)

        # x1, y1, x2, y2 = function(m, n, h, matrix)
        end_time = time.time()
        elapsed_time = end_time - start_time
        times.append(elapsed_time)

    print("End")

    return times


def convert_input(m, n, h, k, matrix, is_prob3=False):
    if is_prob3:
        input_str = f"{m} {n} {h} {k}\n"
    else:
        input_str = f"{m} {n} {h}\n"

    for row in matrix:
        input_str += " ".join(str(x) for x in row) + "\n"

    # Encode the string as bytes
    input_bytes = input_str.encode('utf-8')
    return input_bytes


def calculate_time_taken(file_list):
    all_times = {}
    labels = []
    for filename in file_list:
        times = helper_function(filename, ip_sizes)
        all_times[filename] = times
        labels.append(filename)
        print(times)
        print(labels)

    print(all_times)
    return all_times


def generate_plots(times, files):
    print("Times:", times, "Files:", files)
    plt.plot(ip_sizes, times[files[0]], label=files[0])
    plt.plot(ip_sizes, times[files[1]], label=files[1])
    plt.plot(ip_sizes, times[files[2]], label=files[2])

    plt.xlabel("Input size")
    plt.ylabel("Running time")
    plt.title('Experimental Study')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    all_times = calculate_time_taken(file_list_1)
    generate_plots(all_times, file_list_1)

    all_times = calculate_time_taken(file_list_2)
    generate_plots(all_times, file_list_2)

    all_times = calculate_time_taken(file_list_3)
    generate_plots(all_times, file_list_3)
