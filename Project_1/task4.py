"""Strat4 Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses that are
available that day, paint the house that will stop being available the earliest. (i.e. choose earliest end date
first) """
import heapq


# TC : O(n + m log(m))
def count_houses_strategy4(schedule, days, houses):
    painted_houses = {}
    index = 0
    for day in range(1, days + 1):
        available_houses = []

        # Paint houses available on the current day
        while index < len(schedule) and schedule[index][0] <= day <= schedule[index][1]:
            start, end = schedule[index]
            # Maintain minheap of unpainted houses by end date
            heapq.heappush(available_houses, (end, start, index))
            index += 1

        # Paint the house with the earliest end date
        if available_houses:
            end, start, index = heapq.heappop(available_houses)
            painted_houses[index] = start, end

    return painted_houses
