"""
....#.....
 .........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...

[
['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
]

Process finished with exit code 0
"""
from typing import Tuple, List, Set

MAPPING = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}                       # mapping for the direction of the guard

MOVES = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

def get_start_position_of_guard(field) -> Tuple[int, int, str]:
    for i, row in enumerate(field):
        for j, entry in enumerate(row):
            if entry in MAPPING:
                return i, j, entry


def simulate_guard_movement(field: List[List[str]]) -> int:
    start = get_start_position_of_guard(field)

    pos = (start[0], start[1])
    direction = start[2]

    visited = [row[:] for row in field]
    count = 0

    visited[pos[0]][pos[1]] = 'X'
    count += 1

    while True:
        delta = MOVES[direction]
        next_pos = (pos[0] + delta[0], pos[1] + delta[1])

        if (next_pos[0] < 0 or next_pos[0] >= len(field) or
                next_pos[1] < 0 or next_pos[1] >= len(field[0])):
            break

        if field[next_pos[0]][next_pos[1]] == '#':
            direction = MAPPING[direction]
            continue

        pos = next_pos

        if visited[pos[0]][pos[1]] != 'X':
            visited[pos[0]][pos[1]] = 'X'
            count += 1

    return count


if __name__ == '__main__':
    with open('day6_input.txt') as file:
        map = []
        content = file.read().split('\n')
        for line in content:
            map.append(list(line))

    result = simulate_guard_movement(map)
    print(result)
