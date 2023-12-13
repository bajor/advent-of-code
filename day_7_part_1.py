import re

# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2.
"""
algo:
    - stworz dla kazdego typu algo i przyporzadkuj w pierwszym sorcie hand do typu
    - zrob ranking dla kazdego typu oddzielnie
    - stworz liste pokolei dolaczajac od najslablszsego typu do najmocniejszego
"""


# with open("day_7.txt") as file:
with open("test.txt") as file:
    lines = [x.strip() for x in file]


def is_five_of_kind(cards):
    if all(x == cards[0] for x in cards):
        return cards[0]


def is_four_of_kind(cards):
    if (cards.count(cards[0]) == 4):
        remaining = [x for x in cards if x != x[0]]
        return cards[0], remaining
    if (cards.count(cards[1]) == 4):
        remaining = [x for x in cards if x != x[1]]
        return cards[1], remaining


def is_full_house(cards):
    if len(cards) != 5:
        return False
    char_counts = {}
    for char in cards:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    values = list(char_counts.values())
    return (3 in values and 2 in values) or (2 in values and 3 in values)


def is_pairs(cards, pairs_amount):
    if len(cards) != 5:
        return False
    char_counts = {}
    for char in cards:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    pair_count = sum(count // 2 for count in char_counts.values())
    return pair_count == pairs_amount


def is_two_pairs(cards):
    return is_pairs(cards, 2)


def is_one_pair(cards):
    return is_pairs(cards, 1)


def rank_card(card):
    if card == "a":
        return 0
    elif card == "k": 
        return 1
    elif card == "q":
        return 2
    elif card == "j":
        return 3
    elif card.isdigit():
        return int(card) * -1


five_of_kind = []
four_of_kind = []
full_house = []
two_pairs = []
one_pair = []
high_card = []

lines = [x.split(" ") for x in lines]
lines = [[x, int(y)] for x, y in lines]

for i in range(len(lines)):
    if is_five_of_kind(lines[i][0]):
        five_of_kind.append(lines[i])
        continue
    if is_four_of_kind(lines[i][0]):
        four_of_kind.append(lines[i])
        continue
    if is_full_house(lines[i][0]):
        full_house.append(lines[i])
        continue
    if is_two_pairs(lines[i][0]):
        two_pairs.append(lines[i])
        continue
    if is_one_pair(lines[i][0]):
        one_pair.append(lines[i])
        continue
    high_card.append(lines[i])


# five_of_kind = sorted(five_of_kind, key=sort_five_of_kind)

# four_of_kind = [["".join(sorted(x)), y] for x, y in four_of_kind]
# four_of_kind = sorted(four_of_kind, key=sort_figure_or_number)


for p in four_of_kind:
    print(p)

# dla wszystkich - w kroku is_something - zwroc juz mapowany rank card np dla fulla (q,6) co bedzie znaczylo, ze qqq66 reka
# dla five of kind - zmapuj wszystko na rank card, posortuj same karty po ręce i posortuj ręki