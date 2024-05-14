"""
file:
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet


O/p: 12 + 38 + 15 + 77 = 142
"""


def calibration_values(inp: str) -> int:
    first_digit = last_digit = None
    for i in inp:
        if i.isdigit():
            if first_digit is None:
                first_digit = i
            last_digit = i
    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    else:
        return 0


if __name__ == '__main__':
    total = 0
    with open('trebuchet_ip.txt') as file:
        for line in file:
            total += calibration_values(inp=line.strip())
    print(total)
