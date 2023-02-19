"""
Strategy 2: Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses
that are available that day, paint the house that started being available the latest.
"""
from heapq import heappush, heappop

def countHouses(schedule, n):
  m = len(schedule)

  h = []
  for i in range(m):
    [startTime, endTime] = schedule[i]
    heappush(h, [endTime, startTime])

  i = 0
  j = 0
  houses = 0
  while i <= n:
    if j >= m: break
    [endTime, startTime] = heappop(h)
    if startTime <= n: i = startTime
    print("{} {}",startTime,endTime)
    if i >= startTime  and i <= endTime:
      houses += 1
    j += 1
    i += 1
    print("ha {}" , houses)
  return houses


n, m = map(int, input().split())
schedule = []
for i in range(m):
  startTime, endTime = map(int, input().split())
  schedule.append([startTime, endTime])
noOfHouses = countHouses(schedule, n)
print(noOfHouses)
