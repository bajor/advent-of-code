with open("day_14.txt") as file:
# with open("test.txt") as file:
    lines = [list(x.strip()) for x in file]

CYCLES = 10
# CYCLES = 1000000000


def east(line):
    os = []
    dots = []
    result = []

    for x in line:
        if x == ".":
            dots.extend(x)
        if x == "O":
            os.extend(x)
        if x == "#":
            result.extend(dots)
            result.extend(os)
            result.extend(x)
            os = []
            dots = []

    result.extend(dots)
    result.extend(os)
    return result


def west(line):
    os = []
    dots = []
    result = []

    for x in line:
        if x == ".":
            dots.extend(x)
        if x == "O":
            os.extend(x)
        if x == "#":
            result.extend(os)
            result.extend(dots)
            result.extend(x)
            os = []
            dots = []

    result.extend(os)
    result.extend(dots)
    return result


def north(lines, col_index):
    column = [x[col_index] for x in lines]
    column = west(column)
    for i in range(len(lines)):
        lines[i][col_index] = column[i]
    return lines


def south(lines, col_index):
    column = [x[col_index] for x in lines]
    column = east(column)
    for i in range(len(lines)):
        lines[i][col_index] = column[i]
    return lines


def perform_cycle(lines):
    for i in range(len(lines[0])):
        lines = north(lines, i)
    lines = [west(x) for x in lines]
    for i in range(len(lines[0])):
        lines = south(lines, i)
    lines = [east(x) for x in lines]
    return lines


for i in range(CYCLES):
    if i % 1000 == 0:
        print(i)

    lines = perform_cycle(lines)

for l in lines:
    print("".join(l))