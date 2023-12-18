with open("day_9.txt") as file:
    lines = [x.strip() for x in file]

lines = [line.split(" ") for line in lines]
lines = [[int(x) for x in line] for line in lines]


def seq_differences(seq):
    result = []
    for i in range(len(seq) - 1):
        result.append(seq[i + 1] - seq[i])
    return result


def get_steps_to_zeros(seq):
    steps = [seq]
    while not all([x == 0 for x in seq]):
        seq = seq_differences(seq)
        steps.append(seq)
    return steps


def predict_next_value(steps):
    last_number = None
    for i in range(len(steps) - 1, -1, -1):
        if not last_number:
            last_number = steps[i][-1]
        else:
            last_number = steps[i][-1] + last_number
    return last_number


def predict_next_values(seq):
    steps = get_steps_to_zeros(seq)
    return predict_next_value(steps)


lines = [predict_next_values(x) for x in lines]
print(sum(lines))
