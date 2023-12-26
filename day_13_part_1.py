import copy 


with open("test.txt") as file:
# with open("day_13.txt") as file:
    lines = [x.strip() for x in file]


def create_vertical_lists(lines):
    vertical = []

    for index in range(len(lines[0])):
        vert = []
        for line in lines:
            vert.append(line[index])
        vertical.append(vert)
    return vertical


def generate_split_pairs(lines):
    pairs = []

    for split in range(0, len(lines)):
        first = lines[:split]
        second = lines[split:]
        size = min(len(first), len(second))

        if size == 1:
            first = first[-1:]
            second = second[:1]

            # if len(lines) > 1:
            first = ["".join(l) for l in first]
            second = ["".join(l) for l in second]

        else:
            first = first[-2:]
            second = second[:2]

            first = ["".join(l) for l in first]
            second = ["".join(l) for l in second]
            # if len(lines) > 1:
            #     lines = ["".join(l) for l in lines]

        if first and second:
            pairs.append([first, second])

    # print(pairs)
    # print(" ")

    return pairs


def find_mirrors(pairs):
    for i in range(len(pairs)):
        first_lines, second_lines = pairs[i] 
        second_lines = second_lines[::-1]

        if first_lines == second_lines:
            return i
    return 0


def find_mirror_position(lines):
    pairs_to_check = generate_split_pairs(lines)
    split_position = find_mirrors(pairs_to_check)
    return split_position


def calculate_puzzle(lines):
    horizontal = lines
    vertical = create_vertical_lists(lines)

    mirror_position_v = find_mirror_position(vertical)
    mirror_position_h = find_mirror_position(horizontal)


    if mirror_position_h == 0 and mirror_position_v == 0:
        # print(lines)
        for l in lines:
            print("".join(l))

        print("    ")

    # print(mirror_position_v, mirror_position_h)


    result = mirror_position_h + mirror_position_v * 100
    return result


def split_lines_into_puzzles(lines):
    cumulated = []
    puzzles = []

    for l in lines:
        if l == "":
            puzzles.append(cumulated) 
            cumulated = []
        else:
            cumulated.append(l)
    puzzles.append(cumulated)
    return puzzles 


puzzles = split_lines_into_puzzles(lines)
total = 0


for p in puzzles:
    total += calculate_puzzle(p)

print(total)


# 5334 - too low 
# 28530 - too high
# 22972 - not correcct

# 27505 correct

### !!! some pairs are as list but most are as strings !!!