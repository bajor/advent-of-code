def split_range(start, end, map_ranges):
    breaking_start = []
    breaking_end = []
    breaking_points = []

    for c in map_ranges:
        breaking_start.append(c[0])
        breaking_end.append(c[1])
        for p in c:
            breaking_points.append(p)

    # Ensure that the start is less than or equal to the end
    if start > end:
        raise ValueError("Start must be less than or equal to end")

    # Sort breaking points in ascending order
    breaking_points.sort()

    # Initialize a list to store the split ranges
    split_ranges = []

    # Initialize variables to keep track of the current start and end of the range
    current_start = start
    current_end = end

    # Iterate through breaking points
    for point in breaking_points:
        # Check if the breaking point is within the current range
        if current_start <= point <= current_end:
            # Split the range at the breaking point
            split_ranges.append([current_start, point])
            current_start = point

    # Add the remaining part of the range, if any
    if current_start < current_end:
        split_ranges.append([current_start, current_end])

    for i in range(len(split_ranges)):

        if split_ranges[i][0] in breaking_end:
            split_ranges[i][0] = split_ranges[i][0] + 1

        if split_ranges[i][1] in breaking_start:
            split_ranges[i][1] = split_ranges[i][1] - 1

        if split_ranges[i][0] == split_ranges[i][1]:
            split_ranges[i] = split_ranges[i][0]

    return split_ranges

# Example usage:
start_range =1 
end_range =20 
# breaking_points = [3, 5, 7]

maps_ranges = [[3, 7], [9, 11], [13,17]]

result = split_range(start_range, end_range, maps_ranges)
print(result)
