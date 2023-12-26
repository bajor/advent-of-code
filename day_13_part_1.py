import copy 


# with open("test.txt") as file:
with open("day_13.txt") as file:
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

    for split in range(1, len(lines)):
        first = lines[:split]
        second = lines[split:]

        # print(first)
        # print(second)
        # print(" ")

        size = min(len(first), len(second))

        if size == 1:
            first = first[-1:]
            second = second[:1]
        else:
            first = first[-size:]
            second = second[:size]

        if first and second:
            pairs.append([first, second])

    # for p in pairs:
        # print(len(p[0]), len(p[1]))
    # print(" ")

    return pairs


def find_mirrors(pairs):
    for i in range(len(pairs)):
        first_lines, second_lines = pairs[i] 
        second_lines = second_lines[::-1]

        if first_lines == second_lines:
            return i + 1
    return 0


def find_mirror_position(lines):
    pairs_to_check = generate_split_pairs(lines)
    split_position = find_mirrors(pairs_to_check)
    return split_position


def calculate_puzzle(lines):
    horizontal = lines
    vertical = create_vertical_lists([lines])

    mirror_position_v = find_mirror_position(vertical)
    mirror_position_h = find_mirror_position(horizontal)


    # if not mirror_position_h and not mirror_position_v:
        # print(lines)
        # for l in lines:
            # print("".join(l))
        # print(" ")
    if mirror_position_h == 0 and mirror_position_v == 0:
        # print(lines)
        for l in lines:
            print("".join(l))
        print("    ")

    return mirror_position_h + mirror_position_v * 100

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