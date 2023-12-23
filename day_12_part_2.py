import functools


with open("day_12.txt") as file:
    lines = [x.strip() for x in file]


@functools.cache
def find_arrangements(remaining_springs, remaining_numbers):
    if not remaining_springs and not remaining_numbers:
        return 1 
    if not remaining_springs and remaining_numbers:
        return 0

    current_char = remaining_springs[0]

    if current_char == ".":
        return find_arrangements(remaining_springs[1:], remaining_numbers)

    if current_char == "#":
        if not remaining_numbers:
            return 0
        current_number = remaining_numbers[0]
        if current_number > len(remaining_springs):
            return 0

        if set(remaining_springs[:current_number]).issubset({"?", "#"}) and len(remaining_springs) == current_number:
            return find_arrangements(remaining_springs[current_number:], remaining_numbers[1:])
        if set(remaining_springs[:current_number]).issubset({"?", "#"}) and set(remaining_springs[current_number]).issubset({"?", "."}): 
            return find_arrangements(remaining_springs[current_number+1:], remaining_numbers[1:])
        return 0

    if current_char == "?":
        return find_arrangements(remaining_springs[1:], remaining_numbers) + find_arrangements("#" + remaining_springs[1:], remaining_numbers)


total_count = 0

for l in lines:
    numbers = l.split()[1].split(",")
    numbers = tuple([int(x) for x in numbers])
    numbers = 5*numbers

    springs = l.split()[0]
    springs = "?" + springs
    springs = 5 * springs
    springs = springs[1:]

    total_count += find_arrangements(springs, numbers)

print(total_count)