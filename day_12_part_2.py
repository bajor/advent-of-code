"""
if current char is . -> find() with list[1:] 

# zjadamy po kolei elementy z listy i sprawdzamy czy spelnione sa warunki 
    # jesli spelnione sa warunki to robimy recursive call zjadajac wlasnie ten prawidlowy kawalek listy i listy remaining i idac dalej

    # jesli kolejny krok to ? to robimy 2 recursive calle po kolei, jesen zestepujac go jako ., drugi zastepujac go jako #
"""


# with open("day_12.txt") as file:
with open("test.txt") as file:
    lines = [x.strip() for x in file]


total_count = 0


def find_arrangements(remaining_springs, remaining_numbers):

    # base case  
    if remaining_springs == "" and remaining_numbers != []:
        return 0
    if remaining_springs == "" and remaining_numbers == []:
        return 1

    current_char = remaining_springs[0]
    current_number = remaining_numbers[0]

    if current_number >= len(remaining_springs):
        return 0

    if current_char == ".":
        find_arrangements(remaining_springs[1:], remaining_numbers)

    if current_char == "#":

        if set(remaining_springs[:current_number]).issubset({"?", "#"}) and set(remaining_springs[current_number]).issubset({"?", "."}):
            find_arrangements(remaining_springs[current_number+1:], remaining_numbers[1:])
        else:
            return 0

    if current_char == "?":
        remaining_springs = "." + remaining_springs[1:]
        find_arrangements(remaining_springs, remaining_numbers)

        remaining_springs = "#" + remaining_springs[1:]
        find_arrangements(remaining_springs, remaining_numbers)

    print(remaining_springs, remaining_numbers)


for l in lines:
    numbers = l.split()[1].split(",")
    numbers = [int(x) for x in numbers]
    springs = l.split()[0]
    total_count += find_arrangements(springs, numbers)
    break