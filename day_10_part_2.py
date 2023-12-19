with open("day_10.txt") as file:
    lines = [x.strip() for x in file]


MAX_ROWS = len(lines)
MAX_COLS = len(lines[0])

lines = [list(line) for line in lines]

cells = {}

for i in range(MAX_ROWS):
    for j in range(MAX_COLS):
        cells[(i, j)] = lines[j][i]


coords_arrow = {(-1, 0): "right", (1, 0): "left", (0, -1): "up", (0, 1): "down"}


symbol_move = {
    "|": lambda x, y: [(x, y - 1), (x, y + 1)],
    "-": lambda x, y: [(x - 1, y), (x + 1, y)],
    "L": lambda x, y: [(x, y - 1), (x + 1, y)],
    "J": lambda x, y: [(x, y - 1), (x - 1, y)],
    "7": lambda x, y: [(x, y + 1), (x - 1, y)],
    "F": lambda x, y: [(x, y + 1), (x + 1, y)],
}


inner_area_symbol_direction = {
    ("|", "down"): lambda x, y: [(x + 1, y)],
    ("|", "up"): lambda x, y: [(x - 1, y)],
    ("-", "right"): lambda x, y: [(x, y + 1)],
    ("-", "left"): lambda x, y: [(x, y - 1)],
    ("L", "up"): lambda x, y: [(x - 1, y), (x - 1, y + 1), (x, y + 1)],
    ("L", "left"): lambda x, y: [(x + 1, y - 1)],
    ("J", "up"): lambda x, y: [(x - 1, y - 1)],
    ("J", "right"): lambda x, y: [(x, y + 1), (x + 1, y + 1), (x + 1, y)],
    ("7", "down"): lambda x, y: [(x, y - 1), (x + 1, y - 1), (x + 1, y)],
    ("7", "right"): lambda x, y: [(x - 1, y + 1)],
    ("F", "down"): lambda x, y: [(x + 1, y + 1)],
    ("F", "left"): lambda x, y: [(x - 1, y), (x - 1, y - 1), (x, y - 1)],
}


def find_possible_moves(cell, symbol):
    func = symbol_move[symbol]

    possible_moves = func(*cell)

    for x, y in possible_moves:
        if not 0 <= x <= MAX_COLS:
            return False
        if not 0 <= y <= MAX_ROWS:
            return False

    return possible_moves


def find_s(lines):
    for i in range(MAX_ROWS):
        for j in range(MAX_COLS):
            if lines[j][i] == "S":
                return (i, j)


def find_possible_starts(s_pos):
    possible_start = []

    if 0 < s_pos[0]:
        possible_start.append((s_pos[0] - 1, s_pos[1]))
    if s_pos[0] < MAX_COLS:
        possible_start.append((s_pos[0] + 1, s_pos[1]))
    if 0 < s_pos[1]:
        possible_start.append((s_pos[0], s_pos[1] - 1))
    if s_pos[1] < MAX_COLS:
        possible_start.append((s_pos[0], s_pos[1] + 1))

    return possible_start


def is_possible_cell(cell):
    if 0 <= cell[0] < MAX_COLS and 0 <= cell[1] < MAX_ROWS:
        return True


def perform_walk(staring_pos, previous_cell):
    inner_cells = []

    current_cell = staring_pos
    current_cell_symbol = cells[current_cell]

    walk_history = [(staring_pos, current_cell_symbol)]

    while True:
        if current_cell_symbol == ".":
            return False

        possible_moves = find_possible_moves(current_cell, current_cell_symbol)
        if not possible_moves:
            return False

        possible_moves.remove(previous_cell)

        previous_cell = current_cell
        current_cell = possible_moves[0]
        current_cell_symbol = cells[current_cell]

        move_difference = (
            previous_cell[0] - current_cell[0],
            previous_cell[1] - current_cell[1],
        )
        move_difference = coords_arrow[move_difference]

        inner_cells.append(
            find_innner_cells(current_cell, current_cell_symbol, move_difference)
        )

        walk_history.append((current_cell, current_cell_symbol))

        if current_cell_symbol == "S":
            return walk_history, inner_cells


def find_innner_cells(current_cell, symbol, direction):
    if symbol != "S":
        inner_cells = inner_area_symbol_direction[(symbol, direction)]
        inner_cells = inner_cells(*current_cell)
        inner_cells = [cell for cell in inner_cells if is_possible_cell(cell)]
        return inner_cells


def draw(path):
    cell_drawing = [[" "] * MAX_ROWS for _ in range(MAX_COLS)]
    for cell in path:
        x = cell[0][0]
        y = cell[0][1]
        symbol = cell[1]
        cell_drawing[y][x] = symbol
    for cell in cell_drawing:
        print("".join(cell))


cell = find_s(lines)
starts = find_possible_starts(cell)
pipe_path, inner_cells = perform_walk(starts[2], cell)


def prepare_inner_cells_to_draw(inner_cells):
    result = []
    for cell in inner_cells:
        if cell:
            result.append((cell, "X"))
    return result


draw(pipe_path)

pipe_path = [x[0] for x in pipe_path]
uniqie_inner_cells = []

for cell in inner_cells:
    if cell:
        uniqie_inner_cells.extend(cell)

uniqie_inner_cells = set(uniqie_inner_cells)
pipe_path = set(pipe_path)
uniqie_inner_cells = uniqie_inner_cells.difference(pipe_path)
uniqie_inner_cells = list(uniqie_inner_cells)
inner_cells = prepare_inner_cells_to_draw(uniqie_inner_cells)

draw(inner_cells)


file_path = 'day_10_drawing.txt'
characters = ['X', 'A']

with open(file_path, 'r') as file:
    content = file.read()
    occurrences = {char: content.count(char) for char in characters}

for char, count in occurrences.items():
    print(f"Occurrences of '{char}': {count}")