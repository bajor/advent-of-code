# napisac tak zeby byl z jednego miejsca cache, robic reverse do niego
# i potem reverse back, byle byl jeden cache per 1 linia

with open("test.txt") as file:
    lines = ([list(x.strip()) for x in file])

max_rows = len(lines)
max_cols = len(lines[0])
lines_dict = {}

for y in range(len(lines)):
    for x in range(len(lines[y])):
        lines_dict[(x,y)] = lines[y][x]


def display_dict(lines_dict):
    result = []
    for col in range(max_cols):
        temp_row = []        
        for row in range(max_rows):
            temp_row.append(lines_dict[(row, col)])
        result.append(temp_row)
    for r in result:
        print("".join(r))


display_dict(lines_dict)

