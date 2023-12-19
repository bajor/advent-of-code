"""
- isc po rurze i jakby z prawej strony zabierac wszystkie kropki
- jesli kropka zawiera sie w rurze to jej nie zabierac
- jesli powstale sciezki zamykaja sie - to dodac wszystie kropki wewnatrz zamknietych figur


- tworzymy figury
    grupy polaczonych punktow

- jesli grupa ma licznosc < 9 
aaa
a a
aaa
to dolaczamy do results

- jesli grupa wieksza niz 9:
    - probujemy wypelnic
    - bierzemy TYLKO punkty z danej grupy
    - algo na wypelnianie:
        jesli idziesz z danego punktu do gory w dol, prawo lub w lewo - to w kazdym z tych lini w pewnym momencie napotkasz kropke
        jesli nie napotkasz - to jestes outside



- zrobic druga mape ktora wskazuje "wewnetrzne" kropki dla danych symboli
"""


with open("day_10.txt") as file:
# with open("test.txt") as file:
    lines = [x.strip() for x in file]


MAX_ROWS = len(lines)
MAX_COLS = len(lines[0])

lines = [list(line) for line in lines]

cells = {}

for i in range(MAX_ROWS):
    for j in range(MAX_COLS):
        cells[(i, j)] = lines[j][i]


symbol_move = {
    "|": lambda x, y: [(x, y - 1), (x, y + 1)],
    "-": lambda x, y: [(x - 1, y), (x + 1, y)],
    "L": lambda x, y: [(x, y - 1), (x + 1, y)],
    "J": lambda x, y: [(x, y - 1), (x - 1, y)],
    "7": lambda x, y: [(x, y + 1), (x - 1, y)],
    "F": lambda x, y: [(x, y + 1), (x + 1, y)],
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


def perform_walk(staring_pos, previous_cell):
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

        walk_history.append((current_cell, current_cell_symbol))

        if current_cell_symbol == "S":
            return walk_history


s_pos = find_s(lines)
starts = find_possible_starts(s_pos)
pipe_path = None
correct_start = None

for start in starts:
    try:
        pipe_path = perform_walk(start, s_pos)
        if pipe_path:
            correct_start = start
            break
    except Exception as e:
        print(e)


def draw(path):
    cell_drawing = [[" "] * MAX_ROWS for _ in range(MAX_COLS)]

    for cell in path:
        x = cell[0][0]
        y = cell[0][1]
        symbol = cell[1]
        cell_drawing[y][x] = symbol

    for cell in cell_drawing:
        print("".join(cell))

draw(pipe_path)