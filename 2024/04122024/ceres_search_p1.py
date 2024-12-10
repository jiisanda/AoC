from typing import List


def xmas_in_matrix(matrix: List[List[str]]) -> int:
    # directions = [
    #     (-1, 0), (0, 1), (1, 1),
    #     (-1, 0),         (1, 0),
    #     (-1, -1), (0, -1), (1, -1)
    # ]
    # word = 'XMAS'
    #
    # rows = len(matrix)
    # cols = len(matrix[0])
    #
    # def check_word(x, y, dx, dy):
    #     for i in range(len(word)):
    #         next_x, next_y = x + i * dx, y + i * dy
    #         # print(f"nx: {nx}, ny: {ny}")
    #         if next_x < 0 or next_y < 0 or next_x >= rows or next_y >= cols or matrix[next_x][next_y] != word[i]:
    #             return False
    #     return True
    #
    # count = 0

    rows = len(matrix)
    cols = len(matrix[0])
    word = 'XMAS'
    count = 0

    for y in range(rows):
        for x in range(cols):
            if matrix[y][x] == 'X':
                results = ["" for _ in range(8)]
                # check all eight directions
                # ->
                if x + 3 < cols:
                    results[0] = matrix[y][x] + matrix[y][x+1] + matrix[y][x+2] + matrix[y][x+3]
                # \ (diagonal-right)
                if x + 3 < cols and y + 3 < rows:
                    results[1] = matrix[y][x] + matrix[y+1][x+1] + matrix[y+2][x+2] + matrix[y+3][x+3]
                # | (down)
                if y + 3 < rows:
                    results[2] = matrix[y][x] + matrix[y+1][x] + matrix[y+2][x] + matrix[y+3][x]
                # / (diagonal-left)
                if x - 3 >= 0 and y + 3 < rows:
                    results[3] = matrix[y][x] + matrix[y+1][x-1] + matrix[y+2][x-2] + matrix[y+3][x-3]
                # <-
                if x - 3 >= 0:
                    results[4] = matrix[y][x] + matrix[y][x-1] + matrix[y][x-2] + matrix[y][x-3]
                # \ (diagonal-left - up)
                if x - 3 >= 0 and y - 3 >= 0:
                    results[5] = matrix[y][x] + matrix[y-1][x-1] + matrix[y-2][x-2] + matrix[y-3][x-3]
                # | (up)
                if y - 3 >= 0:
                    results[6] = matrix[y][x] + matrix[y-1][x] + matrix[y-2][x] + matrix[y-3][x]
                # / (diagonal-right - up)
                if x + 3 < cols and y - 3 >= 0:
                    results[7] = matrix[y][x] + matrix[y-1][x+1] + matrix[y-2][x+2] + matrix[y-3][x+3]
                count += results.count(word)

    return count






    # for x in range(rows):
    #     for y in range(cols):
    #         for dx, dy in directions:
    #             if check_word(x, y, dx, dy):
    #                 print(f"Found {word} at {x}, {y}")
    #                 count += 1

    # return count


if __name__ == '__main__':
    with open('test_input.txt') as file:
        content = file.read().split('\n')
        matrix = [list(row) for row in content if row]
        # print(matrix)
    count = xmas_in_matrix(matrix)
    print(count)

