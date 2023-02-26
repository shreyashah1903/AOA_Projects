"""
Strategy 2: Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses
that are available that day, paint the house that started being available the latest.
"""
from heapq import heappush, heappop

# TC : O(n + m log(m))
def count_houses_strategy3(schedule, days, houses):
    painted_houses = {}
    available_houses = []

    house_index = 0
    index = 0
    for day in range(1, days + 1):

        # Paint houses available on the current day
        while house_index < len(schedule) and schedule[house_index][0] <= day <= schedule[house_index][1]:
            start, end = schedule[house_index]
            # Maintain maxheap of unpainted houses by end date
            heappush(available_houses, (end - start, start, end, house_index))
            house_index += 1

        # Paint the house with the latest end date
        if available_houses:
            _, start, end, index1 = heappop(available_houses)
            if start <= day <= end:
                painted_houses[index] = start, end, day, index1
                index += 1

    return painted_houses

# n, m = map(int, input().split())
# schedule = []
# for i in range(m):
#   start_day, end_day = map(int, input().split())
#   schedule.append([start_day, end_day])
# noOfHouses = count_houses(schedule, n)
# print(noOfHouses)
