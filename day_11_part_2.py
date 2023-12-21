from itertools import combinations


with open("day_11.txt") as file:
    matrix = [x.strip() for x in file]


def expand(matrix):
    expanded = []
    for l in matrix:
        if set(l) == set(".") or set(l) == set([".", "*"]):
            expanded.append(len(l) * ["*"])
        else:
            expanded.append(l)
    return expanded


def rotate_matrix_clockwise(matrix):
    transposed_matrix = list(zip(*matrix))
    rotated_matrix = [list(row[::-1]) for row in transposed_matrix]
    return rotated_matrix


def rotate_matrix_counterclockwise(matrix):
    rotated_matrix = [list(row[::-1]) for row in matrix]
    rotated_matrix = list(zip(*rotated_matrix))
    return rotated_matrix


def find_galaxies(matrix):
    galaxies = []
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "#":
                galaxies.append((y, x))
    return galaxies


def shortest_path(start, end, expansions_h, expansions_v):
    distance = abs(start[0] - end[0]) + abs(start[1] - end[1])

    start_x = min(start[0], end[0])
    end_x = max(start[0], end[0])

    start_y = min(start[1], end[1])
    end_y = max(start[1], end[1])

    expansions = []

    for x in range(start_x, end_x):
        if x in expansions_v:
            expansions.append(1)

    for y in range(start_y, end_y):
        if y in expansions_h:
            expansions.append(1)

    expansions_len = len(expansions)

    distance -= expansions_len
    distance += expansions_len * 1000000
    return distance


def find_expansions_v_h(matrix):
    matrix_h = matrix[0]
    matrix_v = [m[0] for m in matrix]

    matrix_h_expansions = []
    matrix_v_expansions = []

    for i in range(len(matrix_h)):
        if matrix_h[i] == "*":
            matrix_h_expansions.append(i)

    for i in range(len(matrix_v)):
        if matrix_v[i] == "*":
            matrix_v_expansions.append(i)

    return matrix_h_expansions, matrix_v_expansions


matrix = [list(l) for l in matrix]
matrix = expand(matrix)
matrix = rotate_matrix_clockwise(matrix)
matrix = expand(matrix)
matrix = rotate_matrix_counterclockwise(matrix)

galaxies = find_galaxies(matrix)
galaxies_combinations = list(combinations(galaxies, 2))

expansions_h, expansions_v = find_expansions_v_h(matrix)

distances = []

for start, end in galaxies_combinations:
    distances.append(shortest_path(start, end, expansions_h, expansions_v))

print(sum(distances))
