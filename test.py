from itertools import combinations

def generate_combinations(balls_number, liczba_wylosowanych):
    balls_ids = list(range(1, balls_number + 1))
    all_combinations = list(combinations(balls_ids, liczba_wylosowanych))
    return all_combinations

balls_number = 20
balls_to_pick = 5

all_combinations = generate_combinations(balls_number, balls_to_pick)

for combination in all_combinations:
    print(f"balls IDs: {combination}")