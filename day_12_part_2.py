with open("day_12.txt") as file:
# with open("test.txt") as file:
    lines = [x.strip() for x in file]


def find_arrangements(remaining_springs, remaining_numbers):
    if not remaining_springs and not remaining_numbers:
        return 1 
    if not remaining_springs and remaining_numbers:
        return 0

    current_char = remaining_springs[0]

    if current_char == ".":
        return find_arrangements(remaining_springs[1:], remaining_numbers)

    # print("a", remaining_numbers, remaining_springs)

    if current_char == "#":
        if not remaining_numbers:
            return 0

        # if len(remaining_springs) <= current_number:
            # return 0
        # print(current_number, remaining_springs)

        current_number = remaining_numbers[0]

        if current_number > len(remaining_springs):
            return 0

        # case gdzie konczy sie poprawnymi wartosciami, nie robica calla na +1 bo to juz koniec

        if set(remaining_springs[:current_number]).issubset({"?", "#"}) and len(remaining_springs) == current_number:
            return find_arrangements(remaining_springs[current_number:], remaining_numbers[1:])

        # print(current_number, len(remaining_springs), remaining_springs)

        if set(remaining_springs[:current_number]).issubset({"?", "#"}) and set(remaining_springs[current_number]).issubset({"?", "."}): 
            return find_arrangements(remaining_springs[current_number+1:], remaining_numbers[1:])
        else:
            return 0

    if current_char == "?":
        return find_arrangements(remaining_springs[1:], remaining_numbers) + find_arrangements("#" + remaining_springs[1:], remaining_numbers)
        

total_count = 0

for l in lines:
    numbers = l.split()[1].split(",")
    numbers = tuple([int(x) for x in numbers])
    springs = l.split()[0]
    total_count += find_arrangements(springs, numbers)
    print(total_count)