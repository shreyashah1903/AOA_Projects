"""
Strategy 1: Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses
that are available to be painted on that day, paint the house that started being available
the earliest.
Strategy 1 should be done in Theta(n) time.
"""


# TC : O(n)
def count_houses_strategy1(schedule, days, houses):
    painted_houses = []
    house_index = 0
    for day in range(1, days + 1):
        if house_index >= houses: break
        [start, end] = schedule[house_index]

        while house_index < len(schedule) - 1 and day > schedule[house_index][1]:
            print("Index index can't paint {}".format(house_index))
            house_index += 1
            [start, end] = schedule[house_index]

        # Paint the house
        if start <= day <= end:
            painted_houses.append([start, end, day, house_index])
            house_index += 1

    return painted_houses

# n, m = map(int, input().split())
# schedule = []
# for i in range(m):
#   startTime, endTime = map(int, input().split())
#   schedule.append([startTime, endTime])
# noOfHouses = count_houses(schedule, n, m)
# print(noOfHouses)
