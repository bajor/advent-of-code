
from itertools import combinations


elements = ["*", "v", "h"]
all_combinations = []
for length in range(1, 4):
    all_combinations.extend(list(combinations(elements, length)))
all_combinations = [set(e) for e in all_combinations]


print(all_combinations)

# [set("*"), set("v"), set("h"), set(["*", "v", "h"]), 