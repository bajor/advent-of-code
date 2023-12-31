with open("day_15.txt") as file:
    values_list = file.read().split(",")


def calculate_hash_char(char, value=0):
    char = ord(char)
    char = (char + value) * 17
    return char % 256


def calculate_hash_list(chars):
    result = 0
    for c in chars:
        result = calculate_hash_char(c, result)
    return result


def generate_hash_map():
    hash_map = {}

    for v in values_list:
        label = v.split("=")[0]
        label = label.split("-")[0]
        key = calculate_hash_list(label) + 1
        value = v[-1]

        if (not key in hash_map) and value.isdigit():
            hash_map[key] = [v]
        elif key in hash_map:
            lenses = hash_map[key]
            lenses = [x.split("=")[0] for x in lenses]
            if key in hash_map:
                if value == "-":
                    if label in lenses:
                        index = lenses.index(label)
                        hash_map[key].pop(index)
                else:
                    if label in lenses:
                        index = lenses.index(label)
                        hash_map[key][index] = v
                    else:
                        hash_map[key].append(v)

    def filter_out_values(values):
        return [int(x[-1]) for x in values]

    hash_map = {k: filter_out_values(v) for k, v in hash_map.items() if v}
    return hash_map


def calculate_lenses(box_id, lenses):
    result = 0
    for i in range(len(lenses)):
        result += box_id * (i + 1) * lenses[i]
    return result


hash_map = generate_hash_map()
result = 0

for k, v in hash_map.items():
    result += calculate_lenses(k, v)

print(result)
