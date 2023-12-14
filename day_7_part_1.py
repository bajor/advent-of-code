import re


with open("day_7.txt") as file:
# with open("test.txt") as file:
    lines = [x.strip() for x in file]


def is_five_of_kind(cards):
    score = cards[1]
    cards = cards[0]
    if all(x == cards[0] for x in cards):
        return cards[0], score


def is_four_of_kind(cards):
    score = cards[1]
    cards = cards[0]
    if (cards.count(cards[0]) == 4):
        remaining = [x for x in cards if x != cards[0]]
        return (cards[0], remaining[0]), score
    if (cards.count(cards[1]) == 4):
        remaining = [x for x in cards if x != cards[1]]
        return (cards[1], remaining[0]), score 


def is_full_house(cards):
    score = cards[1]
    cards = cards[0]
    if len(cards) != 5:
        return False
    char_counts = {}
    for char in cards:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    values = list(char_counts.values())
    if (3 in values and 2 in values) or (2 in values and 3 in values):
        char_counts = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
        char_counts = list(char_counts.keys())
        return (char_counts[0], char_counts[1]), score


def is_three(cards):
    score = cards[1]
    cards = cards[0]
    if len(cards) != 5:
        return False
    char_counts = {}
    for char in cards:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    values = list(char_counts.values())
    if 3 in values:
        char_counts = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
        char_counts = list(char_counts.keys())
        return char_counts[0], (char_counts[1], char_counts[2]), score


def is_pairs(cards, pairs_amount):
    score = cards[1]
    cards = cards[0]
    if len(cards) != 5:
        return False
    char_counts = {}
    for char in cards:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    pair_count = sum(count // 2 for count in char_counts.values())

    if pair_count == pairs_amount and pairs_amount == 2:
        char_counts = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
        char_counts = list(char_counts.keys())
        return (char_counts[0], char_counts[1]), char_counts[2], score

    if pair_count == pairs_amount and pairs_amount == 1:
        char_counts = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
        char_counts = list(char_counts.keys())
        return char_counts[0], (char_counts[1], char_counts[2], char_counts[3]), score


def is_two_pairs(cards):
    return is_pairs(cards, 2)


def is_one_pair(cards):
    return is_pairs(cards, 1)


def rank_card(card):
    if card == "A":
        return 14 
    elif card == "K": 
        return 13 
    elif card == "Q":
        return 12 
    elif card == "J":
        return 11 
    elif card == "T":
        return 10 
    elif card.isdigit():
        return int(card)


five_of_kind = []
four_of_kind = []
full_house = []
three = []
two_pairs = []
one_pair = []
high_card = []

lines = [x.split(" ") for x in lines]
lines = [[x, int(y)] for x, y in lines]

for i in range(len(lines)):
    if is_five_of_kind(lines[i]):
        five_of_kind.append(is_five_of_kind(lines[i]))
        continue
    if is_four_of_kind(lines[i]):
        four_of_kind.append(is_four_of_kind(lines[i]))
        continue
    if is_full_house(lines[i]):
        full_house.append(is_full_house(lines[i]))
        continue
    if is_three(lines[i]):
        three.append(is_three(lines[i]))
        continue
    if is_two_pairs(lines[i]):
        two_pairs.append(is_two_pairs(lines[i]))
        continue
    if is_one_pair(lines[i]):
        one_pair.append(is_one_pair(lines[i]))
        continue
    high_card.append(lines[i])

ranking = []

high_card = [(list(x[0]), x[1]) for x in high_card]
high_card = [([rank_card(y) for y in x[0]], x[1]) for x in high_card]
high_card = [(sorted(x[0], reverse=True), x[1]) for x in high_card]
high_card = [(x[0][0], x[0][1], x[0][2], x[0][3], x[0][4], x[1]) for x in high_card]
high_card = sorted(high_card, key=lambda x: (x[0], x[1], x[2], x[3], x[4]) )
high_card = [x[-1] for x in high_card]
ranking.extend(high_card)

one_pair = [(rank_card(x[0]), sorted((rank_card(x[1][0]), rank_card(x[1][1]), rank_card(x[1][2])), reverse=True), x[2]) for x in one_pair]
one_pair = [(x[0], x[1][0], x[1][1], x[1][2], x[2]) for x in one_pair]
one_pair = sorted(one_pair, key=lambda x: (x[0], x[1], x[2], x[3]) )
one_pair = [x[-1] for x in one_pair]
ranking.extend(one_pair)

two_pairs = [(sorted((rank_card(x[0][0]), rank_card(x[0][1])), reverse=True), rank_card(x[1]), x[2]) for x in two_pairs]
two_pairs = [(x[0][0], x[0][1], x[1], x[2]) for x in two_pairs]
two_pairs = sorted(two_pairs, key=lambda x: (x[0], x[1], x[2]))
two_pairs = [x[-1] for x in two_pairs]
ranking.extend(two_pairs)

three = [(rank_card(x[0]), sorted((rank_card(x[1][0]), rank_card(x[1][1])), reverse=True),  x[2]) for x in three]
three = [(x[0], x[1][0], x[1][1], x[2]) for x in three]
three = sorted(three, key=lambda x: (x[0], x[1], x[2]))
three = [x[-1] for x in three]
ranking.extend(three)

full_house = [(rank_card(x[0][0]), rank_card(x[0][1]),  x[1]) for x in full_house]
full_house = sorted(full_house, key=lambda x: (x[0], x[1]))
full_house = [x[-1] for x in full_house]
ranking.extend(full_house)

four_of_kind = [(rank_card(x[0][0]), rank_card(x[0][1]), x[1]) for x in four_of_kind]
four_of_kind = sorted(four_of_kind, key=lambda x: (x[0], x[1]) )
four_of_kind = [x[-1] for x in four_of_kind]
ranking.extend(four_of_kind)

five_of_kind = [(rank_card(x[0]), x[1]) for x in five_of_kind]
five_of_kind = sorted(five_of_kind, key=lambda x: x[0])
five_of_kind = [x[-1] for x in five_of_kind]
ranking.extend(five_of_kind)

final_score = 0
# print(len(ranking))

for i in range(len(ranking)):
    rank = i + 1
    score = rank * ranking[i]
    final_score += score


print(final_score)
# 199657538
# 200787843 - too low
# 250263225 - too low

for r in ranking:
    print(r)