import re


with open("day_3.txt") as file:
    lines = [x.strip() for x in file]

MAX_LINE_LENGTH = len(lines[0]) - 1
MAX_ROW_NUMBER = len(lines) - 1


def find_numbers_positions_in_row(numbers_positions, row):
    positions = []

    for number_position in numbers_positions:
        start = number_position["start"]
        end = number_position["end"]
        number_position = number_position["number"]
        position = {
            "number": int(number_position),
            "start": start,
            "end": end - 1,
            "row": row,
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
    all_symbols_positions = {}
    for row in range(len(symbols)):
        symbols_positions = find_symbols_positions_in_row(symbols[row])
        if symbols_positions:
            all_symbols_positions[row] = symbols_positions
    return all_symbols_positions


def generate_positions_to_check_per_row(position):
    positions_to_check = {}

    start = position["start"]
    end = position["end"]
    row = position["row"]
    if start != 0:
        start -= 1
    if end != MAX_LINE_LENGTH:
        end += 1
    start_to_end = list(range(start, end + 1))

    positions_to_check[row] = [start, end]
    if row != 0:
        positions_to_check[row - 1] = start_to_end
    if row != MAX_ROW_NUMBER:
        positions_to_check[row + 1] = start_to_end

    return positions_to_check


def filter_numbers_positions(number_positions, symbols_positions):
    filtered = []

    for position in number_positions:
        positions_to_check = generate_positions_to_check_per_row(position)
        if is_touching_symbol(positions_to_check, symbols_positions):
            filtered.append(position["number"])
    return filtered


def is_touching_symbol(possible_symbol_positions, symbol_positions):
    rows_to_check = list(possible_symbol_positions.keys())

    for row in rows_to_check:
        possible_positions = possible_symbol_positions[row]
        if row in symbol_positions:
            positions = symbol_positions[row]
        else:
            positions = []
        if set(possible_positions) & set(positions):
            return True
    return False


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


numbers_pattern = re.compile(r"\d+")
numbers_lines = [re.finditer(numbers_pattern, line) for line in lines]
numbers_lines = prepare_numbers_lines(numbers_lines)
numbers_positions = find_all_numbers_positions(numbers_lines)

symbols_pattern = re.compile(r"[^a-zA-Z0-9.]")
symbols = [re.finditer(symbols_pattern, line) for line in lines]
symbols_positions = find_all_symbols_positions(symbols)

filtered = filter_numbers_positions(numbers_positions, symbols_positions)

print(sum(filtered))
