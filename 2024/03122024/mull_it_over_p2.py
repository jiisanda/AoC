import re
from typing import List, Tuple


def get_conditional_points(instruction: str) -> List[Tuple[int, str | Tuple[str, str]]]:
    all_do = [(m.start(), 'do') for m in re.finditer(r'do\(\)', instruction)]
    all_dont = [(m.start(), 'dont') for m in re.finditer(r"don't\(\)", instruction)]

    all_mulls = [(m.start(), (m.group(1), m.group(2))) for m in re.finditer(r'mul\((\d{1,3}),(\d{1,3})\)', instruction)]

    return sorted(all_do + all_dont + all_mulls)


def get_enabled_mulls(instruction: str):
    conditional_points = get_conditional_points(instruction)
    enabled = True
    valid_mulls = []

    for index, operation in conditional_points:
        if operation == 'do':
            enabled = True
        elif operation == "dont":
            enabled = False
        elif enabled:
            valid_mulls.append(operation)

    return valid_mulls


if __name__ == '__main__':
    added_result = 0
    with open('2024/03122024/day3_input.txt') as file:
        content = file.read()
        enabled_mulls = get_enabled_mulls(content)

    for all_muls in enabled_mulls:
        added_result += int(all_muls[0]) * int(all_muls[1])

    print(added_result)