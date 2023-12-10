with open("day_4.txt") as file:
    lines = [x.strip() for x in file]


def parse_to_lists(line):
    numbers_str = line.split(":")[1].strip().split("|")
    winning_numbers = list(map(int, numbers_str[0].split()))
    my_numbers = list(map(int, numbers_str[1].split()))
    return winning_numbers, my_numbers


def common_size(numbers):
    return len(set(numbers[0]) & set(numbers[1]))


def calculate_score(score):
    if score != 0:
        return 2 ** (score - 1)


lines = [parse_to_lists(x) for x in lines]
lines = [common_size(x) for x in lines]
lines = [calculate_score(x) for x in lines if calculate_score(x)]

print(sum(lines))
