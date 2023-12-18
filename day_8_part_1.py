with open("day_8.txt") as file:
    lines = [x.strip() for x in file]

instructions = list(lines[0])

lines = lines[2:]
lines = [x.split(" = ") for x in lines]
lines = [
    [x[0], tuple(x[1].replace(")", "").replace("(", "").split(", "))] for x in lines
]

nodes = {line[0]: line[1] for line in lines}


current_node = "AAA"
instruction_iter = 0
steps = 0

while current_node != "ZZZ":
    current_instruction = instructions[instruction_iter]

    if current_instruction == "L":
        current_node = nodes[current_node][0]
    if current_instruction == "R":
        current_node = nodes[current_node][1]

    instruction_iter += 1
    if instruction_iter == len(instructions):
        instruction_iter = 0

    steps += 1

print(steps)
