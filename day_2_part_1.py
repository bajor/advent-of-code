with open("day_2.txt") as file:
    lines = [x.strip() for x in file]


def find_max_scores(row):
    game_id = row.split(": ")[0]
    game_id = int(game_id.split("Game ")[1])
    games = row.split(": ")[1].split("; ")

    score = calculate_score(games)

    score["game_id"] = game_id
    return score


def calculate_score(games):
    max_green = 0
    max_red = 0
    max_blue = 0

    for game in games:
        game = game.split(", ")
        for cube in game:
            if "green" in cube:
                max_green = max(max_green, int(cube.split(" ")[0]))
            if "red" in cube:
                max_red = max(max_red, int(cube.split(" ")[0]))
            if "blue" in cube:
                max_blue = max(max_blue, int(cube.split(" ")[0]))

    score = {"max_green": max_green, "max_red": max_red, "max_blue": max_blue}
    return score


def filter_scores(score):
    if score["max_red"] > 12:
        return 0
    if score["max_green"] > 13:
        return 0
    if score["max_blue"] > 14:
        return 0
    return score["game_id"]


result = [find_max_scores(line) for line in lines]
result = [filter_scores(line) for line in result]

print(sum(result))