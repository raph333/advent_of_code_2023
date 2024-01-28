from collections import defaultdict
from enum import Enum
from typing import List, Dict


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


DrawDict = Dict[Color, int]
CUBES = {Color.RED: 12, Color.GREEN: 13, Color.BLUE: 14}


def read_data(file_path: str) -> Dict[int, List[DrawDict]]:
    with open(file_path) as f:
        lines = f.readlines()
    data = defaultdict(list)

    for line in lines:
        game, draws = line.split(":")
        game_id = int(game.replace("Game", "").strip())
        for draw in draws.strip().split(";"):
            cubes = [cube.strip().split(" ") for cube in draw.split(",")]
            data[game_id].append({Color(color): int(num) for num, color in cubes})

    return dict(data)


def draw_possible(draw: DrawDict) -> bool:
    return all(num <= CUBES[color] for color, num in draw.items())


def game_possible(game: List[DrawDict]) -> bool:
    return all(draw_possible(d) for d in game)


games = read_data("input.txt")
print(sum(id_ for id_, game in games.items() if game_possible(game)))
