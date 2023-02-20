"""
Strategy 2: Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses
that are available that day, paint the house that started being available the latest.
"""
from heapq import heappush, heappop

def count_houses(schedule, n, m):
  h = []
  # for i in range(m):
  #   [start_day, end_day] = schedule[i]
  #   heappush(h, [end_day, start_day])

  i = 0
  j = 0
  houses = 0
  while i <= n:
    while j < m:
      [start_day, end_day] = schedule[j]
      if i >= start_day  and i <= end_day:
        heappush(h, [end_day - start_day, start_day, end_day])
        j += 1
      else: break
    if len(h) > 0:
      [_, start_day, end_day] = heappop(h)
      print("Considering index j {} day {}".format(j,i))
      if i >= start_day  and i <= end_day:
        print("Painted house index {} with (start_day, end_day) {}-{},  on day {}".format(j, start_day, end_day, i))
        houses += 1
    i += 1
  return houses


# n, m = map(int, input().split())
# schedule = []
# for i in range(m):
#   start_day, end_day = map(int, input().split())
#   schedule.append([start_day, end_day])
# noOfHouses = count_houses(schedule, n)
# print(noOfHouses)
