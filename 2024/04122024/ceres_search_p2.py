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
            if matrix[y][x] == 'A':
                results = ["" for _ in range(2)]
                # diagonal-right (\)
                if x - 1 >= 0 and y - 1 >= 0 and x + 1 < cols and y + 1 < rows:
                    results[0] = matrix[y-1][x-1] + matrix[y][x] + matrix[y+1][x+1]
                # diagonal-left (/)
                if x - 1 >= 0 and y + 1 < rows and x + 1 < cols and y - 1 >= 0:
                    results[1] = matrix[y+1][x-1] + matrix[y][x] + matrix[y-1][x+1]

                # print(results)
                if results.count('MAS') + results.count('SAM') == 2:
                    print(f"y: {y}, x: {x}")
                    count += 1
                # count += results.count(word)

    return count


if __name__ == '__main__':
    with open('day4_input.txt') as file:
        content = file.read().split('\n')
        matrix = [list(row) for row in content if row]
        # print(matrix)
    count = xmas_in_matrix(matrix)
    print(count)

