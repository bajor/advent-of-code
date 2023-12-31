with open("day_15.txt") as file:
    values = file.read().split(",")


def calculate_hash_char(char, value=0):
    char = ord(char)
    char = (char + value) * 17
    return char % 256


def calculate_hash_list(chars):
    result = 0
    for c in chars:
        result = calculate_hash_char(c, result)
    return result


values = [calculate_hash_list(x) for x in values]
print(sum(values))