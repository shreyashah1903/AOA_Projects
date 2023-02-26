"""
Strategy 5 (Bonus)
"""
from heapq import heappush, heappop


# TC : O(m log(m))
def count_houses_bonus_strategy(schedule, days, houses):
    painted_houses = []
    available_houses = []

    day = 1
    house_index = 0
    while house_index < houses or available_houses:
        if not available_houses:
            if schedule[house_index][0] < 1:
                day = 1
            else:
                day = schedule[house_index][0]

        if day > days: break

        while house_index < houses and schedule[house_index][0] <= day:
            start, end = schedule[house_index]
            heappush(available_houses, (end, start, house_index))
            house_index += 1
        end, start, index = heappop(available_houses)
        painted_houses.append([start, end, day, index])
        day += 1

        while available_houses:
            end, start, index = available_houses[0]
            if end < day:
                heappop(available_houses)
            else: break

    return painted_houses
