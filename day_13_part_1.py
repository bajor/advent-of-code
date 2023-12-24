with open("test.txt") as file:
    lines = [x.strip() for x in file]


def create_vertical_lists(lines):
    vertical = []
    for index in range(len(lines[0])):
        vert = []
        for line in lines:
            vert.append(line[index])
        vertical.append(vert)
    return vertical


def generate_split_pairs(lines):
    # return list of pairs to check 
    pairs = []

    for split in range(1, len(lines)):
        first = lines[:split]
        second = lines[split:]

        size = min(len(first), len(second))

        if size == 1:
            first = first[-1:]
            second = second[:1]
        else:
            first = first[-2:]
            second = second[:2]

        pairs.append([first, second])
        
    return pairs


def find_mirrors(pairs):
    for pair in pairs:
        first_lines, second_lines = pair 

        second_lines = list(reversed(second_lines))

        print(first_lines, second_lines)



horizontal = lines
vertical = create_vertical_lists(lines)

pairs_to_check = generate_split_pairs(horizontal)

find_mirrors(pairs_to_check)


# for p in pairs_to_check:
    # print(p)

