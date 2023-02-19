"""
Strategy 1: Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses
that are available to be painted on that day, paint the house that started being available
the earliest.
Strategy 1 should be done in Theta(n) time.
"""

def countHouses(schedule, n, m):
  j = 0
  houses = 0
  for i in range(1, n+1):
    if j >= m: break
    print("Considering index j {} day {}".format(j,i))
    [startTime, endTime] = schedule[j]
    if i >= startTime  and i <= endTime:
      print("Painted house {}-{} on day {}".format(startTime, endTime, i))
      houses += 1
    elif endTime <= n and i <= endTime: continue
    j +=1
  return houses


