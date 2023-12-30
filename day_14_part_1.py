from itertools import groupby


with open("day_14.txt") as file:
    lines = [x.strip() for x in file]


def create_vertical_lists(lines):
    vertical = []

    for index in range(len(lines[0])):
        vert = []
        for line in lines:
            vert.append(line[index])
        vertical.append(vert)
    return vertical


def divide_into_sublists_and_sort(original_list):
    delimiter = '#'
    sublists = [sorted("".join(list(group)), reverse=True) for _, group in groupby(original_list, lambda x: x == delimiter)]
    return sublists


vertical = create_vertical_lists(lines)
sublists = [divide_into_sublists_and_sort(x) for x in vertical]
joined = ["".join(["".join(e) for e in element]) for element in sublists]

total_load = 0

for column in joined:
    for i in range(len(column)):
        distance = len(column) - i
        if column[i] == "O":
            total_load += distance


print(total_load)
