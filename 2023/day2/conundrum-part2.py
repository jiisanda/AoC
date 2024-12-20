"""
what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

- In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes.
  If any color had even one fewer cube, the game would have been impossible.
- Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
- Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
- Game 4 required at least 14 red, 3 green, and 15 blue cubes.
- Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively.
Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""
import operator
import re

from functools import reduce
from typing import Dict


def process_input(game: str) -> Dict[int, Dict[str, int]]:
    pattern = r'Game \d+: '
    game = re.sub(pattern, '', game)
    sets = game.split(sep="; ")
    result = {}
    for i, s in enumerate(sets, start=1):
        result[i] = {}
        cubes = s.split(', ')
        for cube in cubes:
            if cube:
                count, color = cube.split(' ')
                result[i][color] = int(count)
    return result


def power_of_fewest(inp: str) -> int:
    fewest = {'red': 0, 'blue': 0, 'green': 0}
    game_dict = process_input(game=inp)
    for _, game in game_dict.items():
        for color, value in game.items():
            if value > fewest[color]:
                fewest[color] = value
    return reduce(operator.mul, fewest.values())


if __name__ == '__main__':
    sum_powers = 0
    with (open('2023/day2/conundrum.txt') as file):
        for line in file:
            power_of_game = power_of_fewest(inp=line.strip())
            sum_powers += power_of_game
    print(sum_powers)
