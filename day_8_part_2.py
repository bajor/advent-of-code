import math

with open("day_8.txt") as file:
    lines = [x.strip() for x in file]

instructions = list(lines[0])

lines = lines[2:]
lines = [x.split(" = ") for x in lines]
lines = [
    [x[0], tuple(x[1].replace(")", "").replace("(", "").split(", "))] for x in lines
]

nodes = {line[0]: line[1] for line in lines}
starting_nodes = [line[0] for line in lines if line[0][-1] == "A"]


def find_min_steps(node):
    steps = 0
    instruction_iter = 0

    while node[-1] != "Z":
        current_instruction = instructions[instruction_iter]

        if current_instruction == "L":
            node = nodes[node][0]
        if current_instruction == "R":
            node = nodes[node][1]

        instruction_iter += 1
        if instruction_iter == len(instructions):
            instruction_iter = 0

        steps += 1
    return steps


steps = [find_min_steps(x) for x in starting_nodes]
lcm = math.lcm(*steps)

print(lcm)
