"""
Strat2: Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses
that are available that day, paint the house that started being available the latest.(i.e. choose late end date first)
"""
import heapq


# TC : O(n + m log(m))
def count_houses_strategy2(schedule, days, houses):
    painted_houses = {}
    house_indices = {}

    for day in range(1, days + 1):
        available_houses = []
        for index in range(0, len(schedule)):
            start, end = schedule[index]
            # Avoid already painted houses and houses not available on the current day
            if index in painted_houses or not (start <= day <= end):
                continue
            # Maintain maxheap of unpainted houses by end date
            heapq.heappush(available_houses, (-end, start))
            house_indices[(start, end)] = index
            index += 1

        # Paint the house with the latest end date
        if available_houses:
            end, start = heapq.heappop(available_houses)
            index = house_indices[(start, -end)]
            painted_houses[index] = start, -end

    return painted_houses
