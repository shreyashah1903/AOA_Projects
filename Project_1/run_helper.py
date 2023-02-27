def fetch_input():
    n, m = map(int, input().split())
    schedule = []
    for i in range(m):
        start_time, end_time = map(int, input().split())
        schedule.append([start_time, end_time])

    return n, m, schedule


def print_houses(painted):
    values = []
    for index in range(0, len(painted)):
        start, end, day, house = painted[index]
        values.append(str(house))
    print(' '.join(values))
