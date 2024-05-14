"""
Now
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

here calibration values are 29, 83, 13, 24, 42, 14, and 76.

O/P: 281

some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and
nine also count as valid "digits".

"""

REPLACE_DICT = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}


def process_str(inp: str) -> str:
    mapped = []
    for idx in range(len(inp)):
        if line[idx].isdigit():
            mapped.append(line[idx])

        for key in REPLACE_DICT:
            if inp.startswith(key, idx):
                mapped.append(REPLACE_DICT[key])

    return ''.join(str(i) for i in mapped)


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
    with open('2023/trebuchet_ip.txt') as file:
        for line in file:
            corrected_line = process_str(inp=line.strip())
            total += calibration_values(inp=corrected_line)
    print(total)
