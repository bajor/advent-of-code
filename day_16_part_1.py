# with open("day_16.txt") as file:
with open("test.txt") as file:
    lines = [x.strip() for x in file]


MAX_ROW = len(lines) - 1
MAX_COL = len(lines[0]) - 1

MOVE_DIRS = {
    "up": (0, -1), 
    "down": (0, 1), 
    "right": (1, 0), 
    "left": (-1, 0)
    }


def create_grid_map(lines):
    grid = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            grid[(x, y)] = lines[y][x]
    return grid


def check_if_finish(x, y, history):
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
    # if len(history) > 100:
    #     if len(set(history)) / len(history) < 0.1:
    #         all_walks_histories.extend(history)
    #         return

    if ((current_coords, current_direction)) in checked_coord_dir:
        all_walks_histories.extend(history)
        return
    else:
        checked_coord_dir.append((current_coords, current_direction)) 

    step = MOVE_DIRS[current_direction]

    new_x = current_coords[0] + step[0]
    new_y = current_coords[1] + step[1]

    if check_if_finish(new_x, new_y, history):
        return

    next_direction = find_next_direction(current_direction, (new_x, new_y))

    history.append((new_x, new_y))

    if next_direction == False:
        all_walks_histories.extend(history)
        return

    perform_walk((new_x, new_y), next_direction, history)


GRID = create_grid_map(lines)

start_position = (0,0)
start_direction = "right"

all_walks_histories = [start_position]
checked_coord_dir = []
perform_walk(start_position, start_direction, [])
print(all_walks_histories)

print(len(set(all_walks_histories)))