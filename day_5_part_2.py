maps = {}
seeds = []


with open("day_5.txt", "r") as file:
    for line in file:
        if line.strip():
            if line.lower().startswith("seeds:"):
                seeds = list(map(int, line.split()[1:]))
            elif ":" in line:
                current_header = line[:-6].strip()
                maps[current_header] = []
            else:
                result = list(map(int, line.split()))
                maps[current_header].append(result)


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


def perform_mapping_single_number(source_number, current_stage_maps):
    found_map = None

    for current_map in current_stage_maps[1]:
        min_value = min(current_map[1])
        max_value = max(current_map[1])

        if source_number >= min_value and source_number <= max_value:
            found_map = current_map

    if not found_map:
        return source_number

    source_map = found_map[1]
    target_map = found_map[0]

    difference_from_start = source_number - min(source_map)
    target_number = min(target_map) + difference_from_start
    return target_number


def perform_mapping_range(current_range, current_stage_maps):
    for current_map in current_stage_maps[1]:
        min_value = min(current_map[1])
        max_value = max(current_map[1])

        if isinstance(current_range, list):
            if (current_range[0] >= min_value and current_range[0] <= max_value) or (
                current_range[1] >= min_value and current_range[1] <= max_value
            ):
                source_map = current_map[1]
                target_map = current_map[0]
                difference_from_start = current_range[0] - min(source_map)
                current_range_len = current_range[1] - current_range[0]
                target_start = target_map[0] + difference_from_start
                target_end = target_start + current_range_len

                return [target_start, target_end]
    return current_range


def cut_list(current_range, map_ranges):
    if isinstance(current_range, int):
        return current_range

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

    breaking_points.sort()
    split_ranges = []
    current_start = start
    current_end = end

    for point in breaking_points:
        if current_start <= point <= current_end:
            split_ranges.append([current_start, point])
            current_start = point

    if current_start < current_end:
        split_ranges.append([current_start, current_end])

    for i in range(len(split_ranges)):
        if (split_ranges[i][0] in breaking_end) and (
            split_ranges[i][0] < split_ranges[i][1]
        ):
            split_ranges[i][0] = split_ranges[i][0] + 1
        if (split_ranges[i][1] in breaking_start) and (
            split_ranges[i][1] > split_ranges[i][0]
        ):
            split_ranges[i][1] = split_ranges[i][1] - 1
        if split_ranges[i][0] == split_ranges[i][1]:
            split_ranges[i] = split_ranges[i][0]
    return split_ranges


def perform_stage_mapping(ranges, current_map, current_cut_map):
    results = []
    for current_range in ranges:
        cut_ranges = cut_list(current_range, current_cut_map)

        if isinstance(current_range, int):
            result = perform_mapping_single_number(current_range, current_map)
            results.append(result)
        else:
            for cut_range in cut_ranges:
                result = perform_mapping_range(cut_range, current_map)
                results.append(result)
    return results


def perform_complete_chain_of_mapping(ranges, maps):
    for current_map in maps:
        current_cut_map = current_map[1]
        current_cut_map = [x[1] for x in current_cut_map]
        ranges = perform_stage_mapping(ranges, current_map, current_cut_map)
    return ranges


seeds = [[seeds[i], seeds[i] + seeds[i + 1]] for i in range(0, len(seeds) - 1, 2)]
maps = [
    [header, map_raw_lists_to_ranges(number_list)]
    for header, number_list in maps.items()
]
output = perform_complete_chain_of_mapping(seeds, maps)
result = []

for o in output:
    if isinstance(o, int):
        result.extend([o])
    else:
        result.extend(o)

result = sorted(result)
print(result[1])
