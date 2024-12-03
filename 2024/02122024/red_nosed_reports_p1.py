from typing import List


def is_record_safe(report: List[int]) -> bool:
    # if sorted(report) == report or sorted(report, reverse=True) == report:
    #     for i in range(1, len(report)):
    #         if abs(report[i] - report[i - 1]) < 1 or abs(report[i] - report[i - 1]) > 3:
    #             return False
    #     return True
    # return False          # n2
    asc = True
    dec = True

    for i in range(1, len(report)):
        if report[i] < report[i - 1]:
            asc = False
        if report[i] > report[i - 1]:
            dec = False
        if abs(report[i] - report[i - 1]) < 1 or abs(report[i] - report[i - 1]) > 3:
            return False
    return asc or dec               # n


if __name__ == '__main__':
    safe_records, unsafe_records = 0, 0
    with open('2024/02122024/day2_input.txt') as file:
        for line in file:
            record = list(map(int, line.split()))
            if is_record_safe(record):
                safe_records += 1
            else:
                unsafe_records += 1

    print("safe_records", safe_records)
    print("unsafe_records", unsafe_records)
