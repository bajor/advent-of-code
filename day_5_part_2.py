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


def perform_mapping(source_ranges, current_stage_maps):
    found_maps = [] 

    for current_range in source_ranges: 
        for current_map in current_stage_maps[1]:
            min_value = min(current_map[1])
            max_value = max(current_map[1])

            if (current_range[0] >= min_value and current_range[0] <= max_value) or (current_range[1] >= min_value and current_range[1] <= max_value):
                found_maps.append(current_map)



    # if not found_maps:
    #     return source_range

    # source_map = found_map[1]
    # target_map = found_map[0]

    # difference_from_start = source_range - min(source_map)
    # target_number = min(target_map) + difference_from_start
    # return target_number

def cut_list(start_end, list_of_lists):
    start, end = start_end
    cut_list = [lst for lst in list_of_lists if not (lst[0] > end or lst[1] < start)]
    # Add the missing ranges
    if start < cut_list[0][0]:
        cut_list.insert(0, [start, cut_list[0][0] - 1])
    for i in range(len(cut_list) - 1):
        if cut_list[i][1] < cut_list[i + 1][0] - 1:
            cut_list.insert(i + 1, [cut_list[i][1] + 1, cut_list[i + 1][0] - 1])
    if end > cut_list[-1][1]:
        cut_list.append([cut_list[-1][1] + 1, end])
    return cut_list


def perform_complete_chain_of_mapping(ranges, maps):
    # current_ranges = ranges

    for current_map in maps:
        cutters = current_map[1]
        cutters = [x[1] for x in cutters]

        # print(ranges)

        for current_range in ranges:

            print(current_range)
            print(cutters)
            current_range_cut = cut_list(current_range, cutters)

            # print(12, current_range_cut)
            # ranges = perform_mapping(ranges, current_map)

        1/0
        return ranges


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


