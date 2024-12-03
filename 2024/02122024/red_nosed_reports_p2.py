from typing import List


def is_record_safe(report: List[int]) -> bool:
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


def check_problem_dampener(report: List[int]) -> bool:
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_record_safe(modified_report):
            return True
    return False


if __name__ == '__main__':
    safe_records, unsafe_records = 0, 0
    list_safe_records =[]
    with open('2024/02122024/day2_input.txt') as file:
        for line in file:
            record = list(map(int, line.split()))
            if is_record_safe(record):
                safe_records += 1
                list_safe_records.append(line)
            elif check_problem_dampener(record):
                safe_records += 1
                list_safe_records.append(line)
            else:
                unsafe_records += 1

    print("safe_records", safe_records)
    # print("list_safe_records", list_safe_records)
    # for rec in list_safe_records:
    #     print(rec, end="")
    print("unsafe_records", unsafe_records)
