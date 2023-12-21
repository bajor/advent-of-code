with open("test.txt") as file:
# with open("day_11.txt") as file:
    matrix = [x.strip() for x in file]

matrix = [list(l) for l in matrix]

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


for e in matrix:
    print("".join(e))
print(" ")

matrix = expand(matrix)
matrix = rotate_matrix_clockwise(matrix)
matrix = expand(matrix)
matrix = rotate_matrix_counterclockwise(matrix)


for t in matrix:
    print("".join(t))




