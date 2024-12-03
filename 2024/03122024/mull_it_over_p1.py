import re
from typing import List


def get_mulls(instruction: str) -> List[str]:
    mulls = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', instruction)

    return mulls


if __name__ == '__main__':
    added_result = 0
    with open('2024/03122024/day3_input.txt') as file:
        content = file.read()
        all_mulls = get_mulls(content)

    # print(all_mulls)
    for ints in all_mulls:
        added_result += int(ints[0]) * int(ints[1])

    print(added_result)
