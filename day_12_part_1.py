from itertools import combinations


# with open("day_12.txt") as file:
with open("test.txt") as file:
    lines = [x.strip() for x in file]

"""
groups are always separated by at least one operational spring

# 1. ktore warunki sa juz spelnione dla kazdego wiersza (jest #) - odfiltrowac te
# 2. spełnić warunki które mogą być spełnione tylko przez konkretne komórki np ..?.. zawsze będzie tylko spełnione przez 1 
# 3. napisac validator ktory patrzy czy spelnione dane warunki
# 4. brute force wynegerowac wszstkie kombinacje
# 5. odfiltrowac te ktore spelniaja
"""

def generate_combinations(n, k):
    # ids = list(range(1, n + 1))
    ids = list(range(n))
    all_combinations = list(combinations(ids, k))
    return all_combinations


def generate_possible_positions(q_positions, missing_hashes):
    n = len(q_positions)
    k = missing_hashes

    combinations_ids = generate_combinations(n, k)
    combinations_ids = [list(x) for x in combinations_ids]

    q_positions_map = [[x, p] for x, p in zip(range(len(q_positions)), q_positions)]
    q_positions_map = {x[0] : x[1] for x in q_positions_map}

    for i in range(len(combinations_ids)):
        for j in range(len((combinations_ids[i]))):
            combinations_ids[i][j] = q_positions_map[combinations_ids[i][j]]


    print(q_positions) 
    print(combinations_ids)


    return combinations_ids

    # step 3 - fill in . remaining
    # print(q_positions, missing_hashes)
    pass


lines_combinations = []

for l in lines:
    hash_positions = [i for i, c in enumerate(l) if c == "#"]
    dot_positions = [i for i, c in enumerate(l) if c == "."]
    q_positions = [i for i, c in enumerate(l) if c == "?"]
    contiguous_groups = l.split(" ")[1].split(",")
    contiguous_groups = [int(x) for x in contiguous_groups]

    hash_count = l.count("#")
    missing_hashes = sum(contiguous_groups) - hash_count

    generate_possible_positions(q_positions, missing_hashes)

    # print(missing_hashes)
    # possible_positions = len(q_positions)

    # print(l)
    # print(hash_positions)
    # print(contiguous_groups)

    # generate all missing_hashes possible positions out of all hashes
    # map this to missing hashes positions
    # fill the remaining with .
    # write validator and filter valid

    break
    # brute force wszystkie pozycje 
    # line_combinations 

    # lines_combinations.append((line_combinations, q_positions))

