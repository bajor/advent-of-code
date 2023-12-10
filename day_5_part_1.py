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
                numbers = list(map(int, line.split()))
                maps[current_header].append(numbers)


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


def perform_mapping(source_number, current_stage_maps):
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


def perform_complete_chain_of_mapping(number, maps):
    for current_map in maps:
        number = perform_mapping(number, current_map)
    return number


maps = [
    [header, map_raw_lists_to_ranges(number_list)]
    for header, number_list in maps.items()
]
mapped_numbers = [perform_complete_chain_of_mapping(number, maps) for number in seeds]

print(min(mapped_numbers))
