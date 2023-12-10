maps = {}
seeds = []


# TODO: 
# divide this into ranges for each map. Then map these ranges. Do this iteration for each map. 1 - see what maps we have - based on that divide our ranges to it. Map all ranges (shift values or leave if no corresponding map).


with open("test.txt", "r") as file:
# with open("day_5.txt", "r") as file:
    for line in file:
        if line.strip():
            if line.lower().startswith("seeds:"):
                seeds = list(map(int, line.split()[1:]))
            elif ":" in line:
                current_header = line[:-6].strip()
                maps[current_header] = []
            else:
                numbers = list(map(int, line.split()))
                maps[current_header].append(numbers)


seeds = [[seeds[i], seeds[i] + seeds[i + 1]] for i in range(0, len(seeds) - 1, 2)]

# print(seeds)

def map_raw_lists_to_ranges(numbers):
    for i in range(len(numbers)):
        step = numbers[i][2]
        destination = numbers[i][0]
        source = numbers[i][1]
        numbers[i] = (
            (destination, destination + step - 1),
            (source, source + step - 1),
            step,
        )
    return numbers


def perform_mapping(current_range, current_stage_maps):
    for current_map in current_stage_maps[1]:
        min_value = min(current_map[1])
        max_value = max(current_map[1])

        if (current_range[0] >= min_value and current_range[0] <= max_value) or (current_range[1] >= min_value and current_range[1] <= max_value):
            source_map = current_map[1]
            target_map = current_map[0]

            difference_from_start = current_range[0] - min(source_map)
            current_range_len = current_range[1] - current_range[0]

            target_start = target_map[0] + difference_from_start
            target_end = target_start + current_range_len

            return [target_start, target_end]
    return current_range


def cut_list(current_range, map_ranges):
    start = current_range[0] 
    end = current_range[1] 
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

def perform_complete_chain_of_mapping(ranges, maps):
    for current_map in maps:
        current_cut_map = current_map[1]
        current_cut_map = [x[1] for x in current_cut_map]

        # print("current map ", current_map)
        # print("current ranges ", ranges)

        def perform_stage(ranges, current_map):
            results = []
            for current_range in ranges:
                cut_ranges = cut_list(current_range, current_cut_map)

                print("cut ranges", cut_ranges)

                for cut_range in cut_ranges:

                    print("cut_range, current map ", cut_range, current_map)

                    result = perform_mapping(cut_range, current_map)
                    results.append(result)
            return results


        print("ranges before mapping ", ranges)

        ranges = perform_stage(ranges, current_map) 

        print("ranges after mapping ", ranges)


        1/0

            # for range_

            # TODO: now perform mapping. If range not in map - return as is



    # 1/0


maps = [
    [header, map_raw_lists_to_ranges(number_list)]
    for header, number_list in maps.items()
]



result = None 

output = perform_complete_chain_of_mapping(seeds, maps)
# for seed_range in seeds:
    # if result is None:
    #     result = output
    # if output < result:
    #     result = output


# print(result)


