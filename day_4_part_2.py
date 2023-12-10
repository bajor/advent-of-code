with open("day_4.txt") as file:
    lines = [x.strip() for x in file]


def parse_to_lists(line):
    numbers_str = line.split(":")[1].strip().split("|")
    winning_numbers = list(map(int, numbers_str[0].split()))
    my_numbers = list(map(int, numbers_str[1].split()))
    return winning_numbers, my_numbers


def common_size(numbers):
    return len(set(numbers[0]) & set(numbers[1]))


def add_no_of_copies(line):
    return [line, 1]


lines = [parse_to_lists(x) for x in lines]
lines = [common_size(x) for x in lines]
lines = [add_no_of_copies(x) for x in lines]

for i in range(len(lines)):
    row = lines[i]
    for x in range(i + 1, i + row[0] + 1):
        if x < len(lines):
            lines[x][1] = lines[x][1] + row[1]

lines = [x[1] for x in lines]
print(sum(lines))
