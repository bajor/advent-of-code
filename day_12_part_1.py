from itertools import combinations, groupby


with open("day_12.txt") as file:
    lines = [x.strip() for x in file]


def generate_combinations(n, k):
    ids = list(range(n))
    all_combinations = list(combinations(ids, k))
    return all_combinations


def generate_possible_positions(q_positions, missing_hashes):
    n = len(q_positions)
    k = missing_hashes

    combinations_ids = generate_combinations(n, k)
    combinations_ids = [list(x) for x in combinations_ids]

    q_positions_map = [[x, p] for x, p in zip(range(len(q_positions)), q_positions)]
    q_positions_map = {x[0]: x[1] for x in q_positions_map}

    for i in range(len(combinations_ids)):
        for j in range(len((combinations_ids[i]))):
            combinations_ids[i][j] = q_positions_map[combinations_ids[i][j]]

    return combinations_ids


def count_correct_lines(possible_lines, contiguous_groups):
    validated = []

    for line in possible_lines:
        grouped_periods = ["".join(g) for k, g in groupby(line) if k == "#"]
        grouped_periods = [len(x) for x in grouped_periods]
        validated.append(grouped_periods)

    return validated.count(contiguous_groups)


possible_positions_count = 0

for l in lines:
    q_positions = [i for i, c in enumerate(l) if c == "?"]
    contiguous_groups = l.split(" ")[1].split(",")
    contiguous_groups = [int(x) for x in contiguous_groups]

    hash_count = l.count("#")
    missing_hashes = sum(contiguous_groups) - hash_count

    possible_positions = generate_possible_positions(q_positions, missing_hashes)
    possible_lines = []

    for p in possible_positions:
        line = l.split(" ")[0]
        line = list(line)
        for i in p:
            line[i] = "#"
        line = "".join(line)
        line = line.replace("?", ".")
        possible_lines.append(line)

    possible_positions_count += count_correct_lines(possible_lines, contiguous_groups)

print(possible_positions_count)
