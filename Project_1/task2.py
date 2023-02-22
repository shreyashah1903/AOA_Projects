"""
Strat2: Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses
that are available that day, paint the house that started being available the latest.(i.e. choose late start date first)
"""
import heapq


# TC : O(n + m log(m))
def count_houses_strategy2(schedule, days, houses):
    painted_houses = {}
    available_houses = []

    index = 0
    for day in range(1, days + 1):

        # Paint houses available on the current day
        while index < len(schedule) and schedule[index][0] <= day <= schedule[index][1]:
            start, end = schedule[index]
            # Maintain maxheap of unpainted houses by end date
            heapq.heappush(available_houses, (-start, end, index))
            index += 1

        # Paint the house with the latest end date
        if available_houses:
            start, end, index1 = heapq.heappop(available_houses)
            if start <= day <= end:
                painted_houses[index1] = -start, end, day

    return painted_houses
