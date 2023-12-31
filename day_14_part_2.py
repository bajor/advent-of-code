from functools import cache


with open("day_14.txt") as file:
    lines = tuple([tuple(list(x.strip())) for x in file])


CYCLES = 1000000000


@cache
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
    return tuple(result)


@cache
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
    return tuple(result)


@cache
def north(lines, col_index):
    lines = list(lines)
    column = [x[col_index] for x in lines]
    column = west(tuple(column))
    for i in range(len(lines)):
        lines[i] = list(lines[i])
        lines[i][col_index] = column[i]
        lines[i] = tuple(lines[i])
    return tuple(lines)


@cache
def south(lines, col_index):
    lines = list(lines)
    column = [x[col_index] for x in lines]
    column = east(tuple(column))
    for i in range(len(lines)):
        lines[i] = list(lines[i])
        lines[i][col_index] = column[i]
        lines[i] = tuple(lines[i])
    return tuple(lines)


@cache
def do_north(lines):
    lines = list(lines)
    for i in range(len(lines[0])):
        lines = north(tuple(lines), i)
    return tuple(lines)


@cache
def do_west(lines):
    lines = list(lines)
    lines = [west(tuple(x)) for x in lines]
    return tuple(lines)


@cache
def do_south(lines):
    lines = list(lines)
    for i in range(len(lines[0])):
        lines = tuple(lines)
        lines = tuple(south(lines, i))
    return tuple(lines)


@cache
def do_east(lines):
    lines = list(lines)
    lines = tuple([east(tuple(x)) for x in lines])
    return tuple(lines)


@cache
def perform_cycle(lines):
    lines = do_north(lines)
    lines = do_west(lines)
    lines = do_south(lines)
    lines = do_east(lines)
    return tuple(lines)


for i in range(CYCLES):
    if i % 1000000 == 0:
        print((CYCLES - i) / CYCLES)
    lines = perform_cycle(lines)

for l in lines:
    print("".join(l))

total_load = 0

lines = list(lines)

for i in range(len(lines)):
    lines[i] = "".join(list(lines[i]))

for j in range(len(lines)):
    for i in range(len(lines[0])):
        distance = len(lines) - j
        if lines[j][i] == "O":
            total_load += distance

print(total_load)
