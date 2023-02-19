"""
Strategy 1: Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses
that are available to be painted on that day, paint the house that started being available
the earliest.
Strategy 1 should be done in Theta(n) time.
"""

def countHouses(schedule, n):
  j = 0
  houses = 0
  for i in range(1, n+1):
    if j >= m: break
    print("Considering index j -{} day -{}".format(j,i))
    [startTime, endTime] = schedule[j]
    if i >= startTime  and i <= endTime:
      print("Painted j -{} on day -{}".format(j,i))
      houses += 1
    elif endTime <= n and i <= endTime: continue
    j +=1
  return houses


n, m = map(int, input().split())
schedule = []
for i in range(m):
  startTime, endTime = map(int, input().split())
  schedule.append([startTime, endTime])
noOfHouses = countHouses(schedule, n)
print(noOfHouses)

