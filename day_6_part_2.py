time = 42686985
distance = 284100511221341


def calculate_distances(max_time):
    result = []

    for speed in range(max_time):
        running_time = max_time - speed
        distance = running_time * speed
        result.append(distance)
    return result

result = calculate_distances(time)
result = [x for x in result if x > distance]
ways_to_win = len(result)
print(ways_to_win)