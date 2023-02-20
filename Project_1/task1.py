"""
Strategy 1: Iterate over each day starting from day 1 . . . n. For each day, among the unpainted houses
that are available to be painted on that day, paint the house that started being available
the earliest.
Strategy 1 should be done in Theta(n) time.
"""

def count_houses(schedule, n, m):
  j = 0
  houses = 0
  for i in range(1, n+1):
    if j >= m: break
    # print("Considering index j {} day {}".format(j,i))
    [start_day, end_day] = schedule[j]
    if i >= start_day  and i <= end_day:
      # print("Painted house index {} with (start_day, end_day) {}-{},  on day {}".format(j, start_day, end_day, i))
      houses += 1
    elif end_day <= n and i <= end_day: continue
    j +=1
  return houses

# n, m = map(int, input().split())
# schedule = []
# for i in range(m):
#   startTime, endTime = map(int, input().split())
#   schedule.append([startTime, endTime])
# noOfHouses = count_houses(schedule, n, m)
# print(noOfHouses)


