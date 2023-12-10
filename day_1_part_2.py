with open("day_1.txt") as file:
    lines = [x.strip() for x in file]

replace_pairs = [ 
    ("one", "o1ne"),
    ("two", "t2wo"),
    ("three", "th3ree"),
    ("four", "f4our"),
    ("five", "fi5ve"),
    ("six", "s6is"),
    ("seven", "se7ven"),
    ("eight", "ei8ght"),
    ("nine", "ni9ne"),
]


def replace_chunk(chunk):
    for word, digit in replace_pairs:
        chunk = chunk.replace(word, digit)
    return chunk


def spelled_digits_to_numbers(text):
    text = replace_chunk(text)
    return str(text)


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


result = [spelled_digits_to_numbers(x) for x in lines]
result = [sum_first_last_digit(x) for x in result] 

print(sum(result))