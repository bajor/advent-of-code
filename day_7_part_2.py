import re


with open("day_7.txt") as file:
    lines = [x.strip() for x in file]


def is_five_of_kind(cards_score):
    cards = cards_score[0]
    if all(x == cards[0] for x in cards):
        return cards_score


def is_four_of_kind(cards_score):
    cards = cards_score[0]
    if cards.count(cards[0]) == 4:
        return cards_score
    if cards.count(cards[1]) == 4:
        return cards_score


def is_full_house(cards_score):
    cards = cards_score[0]
    char_counts = {}
    for char in cards:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    values = list(char_counts.values())
    if (3 in values and 2 in values) or (2 in values and 3 in values):
        char_counts = dict(
            sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
        )
        char_counts = list(char_counts.keys())
        return cards_score


def is_three(cards_score):
    cards = cards_score[0]
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
        char_counts = dict(
            sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
        )
        char_counts = list(char_counts.keys())
        return cards_score


def is_pairs(cards_score, pairs_amount):
    cards = cards_score[0]
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
        char_counts = dict(
            sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
        )
        char_counts = list(char_counts.keys())
        return cards_score

    if pair_count == pairs_amount and pairs_amount == 1:
        char_counts = dict(
            sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
        )
        char_counts = list(char_counts.keys())
        return cards_score


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
        return 0
    elif card == "T":
        return 10
    elif card.isdigit():
        return int(card)


def map_cards_to_scores(cards_scores):
    cards_scores = [(list(x), y) for x, y in cards_scores]
    cards_scores = [([rank_card(card) for card in x], y) for x, y in cards_scores]
    return cards_scores


def sort_cards(hands_type):
    hands_type = sorted(
        hands_type, key=lambda x: [x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]]
    )
    return hands_type


def split_j(cards_score, j_count):
    cards_j = list(filter(lambda x: x[0].count("J") == j_count, cards_score))
    cards_no_j = list(filter(lambda x: x[0].count("J") != j_count, cards_score))
    return cards_j, cards_no_j


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


four_to_five_j, four_of_kind = split_j(four_of_kind, 1)
four_to_five_jjjj, four_of_kind = split_j(four_of_kind, 4)

full_to_five_jj, full_house = split_j(full_house, 2)
full_to_five_jjj, full_house = split_j(full_house, 3)

three_to_four_j, three = split_j(three, 1)
three_to_four_jjj, three = split_j(three, 3)

two_pairs_to_full_j, two_pairs = split_j(two_pairs, 1)
two_pairs_to_four_jj, two_pairs = split_j(two_pairs, 2)

one_pair_to_three_j, one_pair = split_j(one_pair, 1)
one_pair_to_three_jj, one_pair = split_j(one_pair, 2)

high_card_to_pair_j, high_card = split_j(high_card, 1)


five_of_kind.extend(four_to_five_j)
five_of_kind.extend(four_to_five_jjjj)
five_of_kind.extend(full_to_five_jj)
five_of_kind.extend(full_to_five_jjj)

four_of_kind.extend(three_to_four_j)
four_of_kind.extend(three_to_four_jjj)
four_of_kind.extend(two_pairs_to_four_jj)

full_house.extend(two_pairs_to_full_j)

three.extend(one_pair_to_three_j)
three.extend(one_pair_to_three_jj)

one_pair.extend(high_card_to_pair_j)


ranking = []

hand_types = [
    high_card,
    one_pair,
    two_pairs,
    three,
    full_house,
    four_of_kind,
    five_of_kind,
]

for hand in hand_types:
    hand = map_cards_to_scores(hand)
    hand = sort_cards(hand)
    ranking.extend(hand)

for i in range(len(ranking)):
    ranking[i] = (i + 1) * ranking[i][1]

print(sum(ranking))
