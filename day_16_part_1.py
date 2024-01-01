# with open("day_16.txt") as file:
with open("test.txt") as file:
    lines = [x.strip() for x in file]


MAX_ROW = len(lines)
MAX_COL = len(lines[0])

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


def perform_walk(current_coords, direction, history):
    direction = MOVE_DIRS[direction]

    new_x = current_coords[0] + direction[0]
    new_y = current_coords[1] + direction[1]

    if new_x < 0 or new_x > MAX_ROW:
        all_walks_histories.append(history)
        return

    if new_y < 0 or new_y > MAX_COL:
        all_walks_histories.append(history)
        return

    # logic for next direction, check what char are we on, return direction
    next_direction = "down"

    history.append((new_x, new_y))
    perform_walk((new_x, new_y), next_direction, history)


grid = create_grid_map(lines)

start_position = (0,0)
start_direction = "right"

all_walks_histories = []

perform_walk(start_position, start_direction, [])

print(all_walks_histories)