"""
Strategy 1: Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses
that are available to be painted on that day, paint the house that started being available
the earliest.
Strategy 1 should be done in Theta(n) time.
"""
from run_helper import fetch_input, print_houses


# TC : O(n)
def count_houses_strategy1(schedule, days, houses):
    painted_houses = []
    house_index = 0
    for day in range(1, days + 1):
        if house_index >= houses:
            break
        [start, end] = schedule[house_index]

        # Skip house which can't be painted if current day > current house endDay
        while house_index < houses - 1 and day > schedule[house_index][1]:
            house_index += 1
            [start, end] = schedule[house_index]

        # Paint the house
        if start <= day <= end:
            painted_houses.append([start, end, day, house_index])
            house_index += 1

    return painted_houses


n, m, schedule = fetch_input()
painted = count_houses_strategy1(schedule, n, m)
print_houses(painted)
