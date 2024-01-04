with open("day_16.txt") as file:
    lines = [x.strip() for x in file]


MAX_ROW = len(lines) - 1
MAX_COL = len(lines[0]) - 1
MOVE_DIRS = {"up": (0, -1), "down": (0, 1), "right": (1, 0), "left": (-1, 0)}


def create_grid_map(lines):
    grid = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            grid[(x, y)] = lines[y][x]
    return grid


def is_finished(coords, history):
    x, y = coords
    if x < 0 or x > MAX_COL:
        all_walks_histories.extend(history)
        return True
    if y < 0 or y > MAX_ROW:
        all_walks_histories.extend(history)
        return True


def find_next_direction(current_direction, coordinates):
    new_tile = GRID[coordinates]

    if new_tile == ".":
        next_direction = current_direction

    if new_tile == "\\":
        if current_direction == "right":
            next_direction = "down"
        if current_direction == "left":
            next_direction = "up"
        if current_direction == "up":
            next_direction = "left"
        if current_direction == "down":
            next_direction = "right"

    if new_tile == "/":
        if current_direction == "right":
            next_direction = "up"
        if current_direction == "left":
            next_direction = "down"
        if current_direction == "up":
            next_direction = "right"
        if current_direction == "down":
            next_direction = "left"

    if new_tile == "|":
        if current_direction == "right" or current_direction == "left":
            perform_walk(coordinates, "up", [])
            perform_walk(coordinates, "down", [])
            return False

        if current_direction == "up" or current_direction == "down":
            next_direction = current_direction

    if new_tile == "-":
        if current_direction == "up" or current_direction == "down":
            perform_walk(coordinates, "right", [])
            perform_walk(coordinates, "left", [])
            return False

        if current_direction == "right" or current_direction == "left":
            next_direction = current_direction

    return next_direction


def perform_walk(current_coords, current_direction, history):
    while not is_finished(current_coords, history):
        if (current_coords, current_direction) in visited:
            all_walks_histories.extend(history)
            return
        else:
            visited.append((current_coords, current_direction))

        step = MOVE_DIRS[current_direction]

        new_x = current_coords[0] + step[0]
        new_y = current_coords[1] + step[1]

        if is_finished((new_x, new_y), history):
            return

        next_direction = find_next_direction(current_direction, (new_x, new_y))

        history.append((new_x, new_y))

        if next_direction == False:
            all_walks_histories.extend(history)
            return

        current_coords = (new_x, new_y)
        current_direction = next_direction


GRID = create_grid_map(lines)

starts = []

for i in range(MAX_COL):
    starts.append([(i, 0), "down"])
    starts.append([(i, MAX_ROW), "down"])

for i in range(MAX_ROW):
    starts.append([(0, i), "right"])
    starts.append([(MAX_COL, i), "left"])

all_results = []
counter = 0

for start_position, start_direction in starts:
    all_walks_histories = [start_position]
    visited = []

    perform_walk(start_position, start_direction, [])

    result = len(set(all_walks_histories))
    all_results.append(result)
    print(round(counter / len(starts), 2))
    counter += 1

print(max(all_results))
