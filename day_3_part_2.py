import re

with open("day_3.txt") as file:
    lines = [x.strip() for x in file]

MAX_COLS = len(lines[0])
MAX_ROWS = len(lines)


def find_numbers_positions_in_row(numbers_positions, row):
    positions = []

    for number_position in numbers_positions:
        start = number_position["start"]
        end = number_position["end"]
        number_position = number_position["number"]
        coordinates = [(row, y) for y in list(range(start, end))]
        position = {
            "number": int(number_position),
            "x_y": coordinates,
        }
        positions.append(position)
    return positions


def find_all_numbers_positions(numbers_positions_lines):
    all_numbers_positions = []

    for i in range(len(numbers_positions_lines)):
        numbers_positions = find_numbers_positions_in_row(numbers_positions_lines[i], i)
        if numbers_positions:
            all_numbers_positions.extend(numbers_positions)
    return all_numbers_positions


def find_symbols_positions_in_row(numbers):
    positions = []
    for number in numbers:
        positions.append(number.start())
    return positions


def find_all_symbols_positions(symbols):
    all_symbols_positions = []

    for row in range(len(symbols)):
        symbols_positions = find_symbols_positions_in_row(symbols[row])
        if symbols_positions:
            for position in symbols_positions:
                all_symbols_positions.append((row, position))
    return all_symbols_positions


def generate_positions_to_check(stars_position):
    i = stars_position[0]
    j = stars_position[1]
    surrounding_points = []

    for x in range(max(0, i - 1), min(MAX_ROWS, i + 2)):
        for y in range(max(0, j - 1), min(MAX_COLS, j + 2)):
            if x != i or y != j:
                surrounding_points.append((x, y))

    return surrounding_points


def prepare_numbers_lines(numbers_lines):
    found_numbers = []

    for line in numbers_lines:
        row = []
        for number in line:
            number_position = {}
            number_position["number"] = number.group()
            number_position["start"] = number.start()
            number_position["end"] = number.end()
            row.append(number_position)
        found_numbers.append(row)
    return found_numbers


def find_all_numbers_intersecting_generated_positions(
    stars_possible_positions, numbers_positions
):
    touching_numbers = []

    for star_coordinate in stars_possible_positions:
        for number_position in numbers_positions:
            if star_coordinate in number_position["x_y"]:
                if not number_position in touching_numbers:
                    touching_numbers.append(number_position)
    return touching_numbers


numbers_pattern = re.compile(r"\d+")
numbers_lines = [re.finditer(numbers_pattern, line) for line in lines]
numbers_lines = prepare_numbers_lines(numbers_lines)
numbers_positions = find_all_numbers_positions(numbers_lines)


stars_pattern = re.compile(r"\*")
stars = [re.finditer(stars_pattern, line) for line in lines]
stars_positions = find_all_symbols_positions(stars)
stars_positions_to_check = [
    generate_positions_to_check(star) for star in stars_positions
]


connected = [
    find_all_numbers_intersecting_generated_positions(stars, numbers_positions)
    for stars in stars_positions_to_check
]
filtered = [x for x in connected if len(x) == 2]

results = 0

for f in filtered:
    pair = []
    for e in f:
        pair.append(e["number"])
    result = pair[0] * pair[1]
    results += result

print(results)