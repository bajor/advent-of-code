from itertools import combinations


with open("day_11.txt") as file:
    matrix = [x.strip() for x in file]


def expand(matrix):
    expanded = []
    for l in matrix:
        if set(l) == set("."):
            expanded.extend([l, l])
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


def shortest_path(grid, start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


matrix = [list(l) for l in matrix]
matrix = expand(matrix)
matrix = rotate_matrix_clockwise(matrix)
matrix = expand(matrix)
matrix = rotate_matrix_counterclockwise(matrix)

galaxies = find_galaxies(matrix)
galaxies_combinations = list(combinations(galaxies, 2))

distances = []

for start, end in galaxies_combinations:
    distances.append(shortest_path(matrix, start, end))

print(sum(distances))
