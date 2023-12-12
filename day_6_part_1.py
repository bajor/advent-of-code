times = [42, 68, 69, 85]
distances = [284, 1005, 1122, 1341]


def calculate_distances(max_time):
    result = []

    for speed in range(max_time):
        running_time = max_time - speed
        distance = running_time * speed
        result.append(distance)
    return result


max_time = times[0]
best_distance = distances[0]
total_ways_to_win = []

for max_time, best_distance in zip(times, distances):
    result = calculate_distances(max_time)
    result = [x for x in result if x > best_distance]
    ways_to_win = len(result)
    total_ways_to_win.append(ways_to_win)

print(
    total_ways_to_win[0]
    * total_ways_to_win[1]
    * total_ways_to_win[2]
    * total_ways_to_win[3]
)
