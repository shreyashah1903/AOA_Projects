def fetch_input():
    n, m = map(int, input().split())
    schedule = []
    for i in range(m):
        startTime, endTime = map(int, input().split())
        schedule.append([startTime, endTime])

    return n, m, schedule


def print_houses(painted):
    for index in range(0, len(painted)):
        start, end, day, house = painted[index]
        print(house)
