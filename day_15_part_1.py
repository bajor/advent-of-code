with open("day_15.txt") as file:
    values = file.read().split(",")


def calculate_hash(char, value=0):
    char = ord(char)
    char = (char + value) * 17
    return char % 256


def calculate_list_hash(chars):
    result = 0
    for c in chars:
        result = calculate_hash(c, result)
    return result


values = [calculate_list_hash(x) for x in values]
print(sum(values))