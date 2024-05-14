"""
Check if the game if possible

IP:
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

O/p:
8

Explanation:
games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration.
However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once;
similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once.
If you add up the IDs of the games that would have been possible, you get 8.
"""
from typing import Dict


def process_input(game: str) -> Dict[str, str]:
    ...


def possible_conundrum(inp: str) -> Dict[str, str]:
    ...


if __name__ == '__main__':
    total = 0
    with open('2023/trial.txt') as file:
        for line in file:
            conundrum = possible_conundrum(inp=line.strip())
            if conundrum["is_it"]:
                total += conundrum["game_id"]
    print(total)
