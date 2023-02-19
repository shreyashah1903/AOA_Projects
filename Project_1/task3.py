"""
Strategy 2: Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses
that are available that day, paint the house that started being available the latest.
"""
from heapq import heappush, heappop

def count_houses(schedule, n):
  m = len(schedule)

  h = []
  # for i in range(m):
  #   [startTime, endTime] = schedule[i]
  #   heappush(h, [endTime, startTime])

  i = 0
  j = 0
  houses = 0
  while i <= n:
    while j < m:
      [startTime, endTime] = schedule[j]
      if i >= startTime  and i <= endTime:
        heappush(h, [endTime - startTime, startTime, endTime])
        j += 1
      else: break
    if len(h) > 0:
      [_, startTime, endTime] = heappop(h)
      print("Considering index j {} day {}".format(j,i))
      if i >= startTime  and i <= endTime:
        print("Painted house index {} with (startTime, endTime) {}-{},  on day {}".format(j, startTime, endTime, i))
        houses += 1
    i += 1
  return houses


n, m = map(int, input().split())
schedule = []
for i in range(m):
  startTime, endTime = map(int, input().split())
  schedule.append([startTime, endTime])
noOfHouses = count_houses(schedule, n)
print(noOfHouses)
