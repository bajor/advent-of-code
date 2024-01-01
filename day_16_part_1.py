# with open("day_16.txt") as file:
with open("test.txt") as file:
    lines = [x.strip() for x in file]

# input as hashmap x,y and symbol
# direction as hashmap - what to add to go in that direction
# function to move - add direction + current coords (add two tuples)     

# going to symbol - pass direction where you come from and 

MAX_ROW = len(lines)
MAX_COL = len(lines[0])


move = {
    "up" : (0,-1),
    "down" : (0,1),
    "right" : (1,0),
    "left" : (-1,0)
}


def create_grid_map(lines):
    grid = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            grid[(x,y)] = r"" + lines[y][x]
    return grid


def perform_move(current_pos, direction):
    direction = move[direction]
    return (current_pos[0] + direction[0], current_pos[1] + direction[1])


grid = create_grid_map(lines)

a = perform_move((1,1), "up")
print(a)
