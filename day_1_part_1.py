with open("day_1.txt") as file:
    lines = [x.strip() for x in file]


def sum_first_last_digit(text):
    first_found = False 
    first = ""
    last = ""
    for char in text:
        if char.isdigit() and not first_found:
            first = char
            first_found = True
        if char.isdigit():
            last = char
    if not first:
        return 0
    return int(first + last)


result = [sum_first_last_digit(x) for x in lines]

print(sum(result))