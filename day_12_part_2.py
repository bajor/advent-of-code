# with open("day_12.txt") as file:
with open("test.txt") as file:
    lines = [x.strip() for x in file]


def find_arrangements(remaining_springs, remaining_numbers):
    if remaining_springs == "" and len(remaining_numbers) > 0:
        return 0
    if remaining_springs == "" and len(remaining_numbers) == 0:
        print("found")
        return 1 

    current_char = remaining_springs[0]
    current_number = remaining_numbers[0]

    if current_number > len(remaining_springs):
        return 0

    if current_char == ".":
        return find_arrangements(remaining_springs[1:], remaining_numbers)

    if current_char == "#":
        if len(remaining_springs) < remaining_numbers[0]:
            return 0
        if not remaining_numbers:
            return 0

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
    break