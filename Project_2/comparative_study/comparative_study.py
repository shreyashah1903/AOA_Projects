import numpy as np
import time
# from Project_2 import task1, task2, task3, task4
# from Project_2 import task5A, task5B, task6, task7A, task7B

input_dir = 'input'
ip_sizes = [10**2]
# ip_sizes = [10**3, 10**4, 10**5, 10**6, 10**7, 10**8]

file_list_1 = ['task1', 'task2', 'task3']
file_list_2 = ['task4', 'task5A', 'task5B']
file_list_3 = ['task6', 'task7A', 'task7B']


def helper_function(filename, ip_sizes):
    # module_name = filename  # Assumes the file has a .py extension
    # module = __import__(ip_sizes)
    # function_name = module.function.__name__
    times = []
    for sz in ip_sizes:
        m, n = sz, sz + sz / 100
        matrix = np.random.randint(20, size=(m, n))
        h, k = 10, 15
        print("hey")
        start_time = time.time()
        x1, y1, x2, y2 = filename.find_square_area(m, n, h, matrix)
        print("hey2")
        end_time = time.time()
        elapsed_time = end_time - start_time
        times.append(elapsed_time)
    return times


def calculate_time_taken(file_list):
    all_times = {}
    for filename in file_list:
        times = helper_function(filename, ip_sizes)
        all_times[filename] = times
        print(times)
    return all_times


t = calculate_time_taken(file_list_1)



