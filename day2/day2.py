CUBES = {"red": 12, "green": 13, "blue": 14}

with open("input.txt", "r") as f:
    lines = f.readlines()


possible_games = []

for line in lines:
    game_id, games = line.replace("Game", "").strip().split(":")
    for draw in games.split(";"):
        for cube in draw.split(","):
            num, color = cube.strip().split(" ")
            if int(num) > CUBES[color]:
                break
        else:
            continue  # move to next draw if cube-loop didn't break
        break
    else:
        possible_games.append(int(game_id))  # if game-loop didn't break

print(possible_games), sum(possible_games)
