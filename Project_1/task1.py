"""
Strategy 1: Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses
that are available to be painted on that day, paint the house that started being available
the earliest.
Strategy 1 should be done in Theta(n) time.
"""


# TC : O(n)
def count_houses_strategy1(schedule, days, houses):
    painted_houses = {}
    index = 0
    for day in range(1, days + 1):
        if index >= houses: break
        [start, end] = schedule[index]

        while index < len(schedule) - 1 and day > schedule[index][1]:
            index += 1
            [start, end] = schedule[index]

        # Paint the house
        if start <= day <= end:
            painted_houses[index] = start, end
            index += 1

    return painted_houses

# n, m = map(int, input().split())
# schedule = []
# for i in range(m):
#   startTime, endTime = map(int, input().split())
#   schedule.append([startTime, endTime])
# noOfHouses = count_houses(schedule, n, m)
# print(noOfHouses)
