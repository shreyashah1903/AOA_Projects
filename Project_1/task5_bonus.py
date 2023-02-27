"""
Strategy 5 (Bonus)
"""
from heapq import heappush, heappop

from run_helper import fetch_input, print_houses


# TC : O(m log(m))
def count_houses_bonus_strategy(schedule, days, houses):
    painted_houses = []
    available_houses = []

    day = 1
    house_index = 0
    # Loop runs for all houses
    while house_index < houses or available_houses:
        if not available_houses:
            # If start day is set to less than 1, set day to 1. Else, set current day to house start day
            if schedule[house_index][0] < 1:
                day = 1
            else:
                day = schedule[house_index][0]

        if day > days:
            break

        # Find houses available on the current day
        while house_index < houses and schedule[house_index][0] <= day:
            start, end = schedule[house_index]
            # Maintain minheap of unpainted houses by end date
            heappush(available_houses, (end, start, house_index))
            house_index += 1

        end, start, index = heappop(available_houses)
        painted_houses.append([start, end, day, index])
        day += 1

        while available_houses:
            end, start, index = available_houses[0]
            # Popping out houses which can't be painted if their end day is less than current day
            if end < day:
                heappop(available_houses)
            else:
                break

    return painted_houses


n, m, schedule = fetch_input()
painted = count_houses_bonus_strategy(schedule, n, m)
print_houses(painted)
