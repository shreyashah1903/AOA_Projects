"""
Strategy2: Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses
that are available that day, paint the house that started being available the latest.(i.e. choose late start date first)
"""
from heapq import heappush, heappop

from run_helper import fetch_input, print_houses


# TC : O(n + m log(m))
def count_houses_strategy2(schedule, days, houses):
    painted_houses = []
    available_houses = []

    house_index = 0
    for day in range(1, days + 1):

        # Find houses available on the current day
        while house_index < len(schedule) and schedule[house_index][0] <= day <= schedule[house_index][1]:
            start, end = schedule[house_index]
            # Maintain maxheap of unpainted houses by start date
            heappush(available_houses, (-start, end, house_index))
            house_index += 1

        # Paint the house with the latest start date
        while available_houses:
            start, end, index = heappop(available_houses)
            # Paint house only if current day lies between house availability (start and end day)
            if start <= day <= end:
                painted_houses.append([-start, end, day, index])
                break

    return painted_houses


n, m, schedule = fetch_input()
painted = count_houses_strategy2(schedule, n, m)
print_houses(painted)

