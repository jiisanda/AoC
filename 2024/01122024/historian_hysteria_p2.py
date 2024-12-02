from typing import List, Dict


def get_sum_of_similarity_score(l1: List[str], record: Dict[int, int]) -> int:
    score = 0
    for i in l1:
        score += int(i) * record[int(i)]

    return score


if __name__ == '__main__':
    list1, list2 = [], []
    record_count = {}
    with open('2024/01122024/day1_input.txt') as file:
        for line in file:
            a, b = line.split()
            list1.append(a)
            list2.append(b)
    for a in list1:
        if a not in record_count:
            record_count[int(a)] = list2.count(a)

    print(get_sum_of_similarity_score(list1, record_count))
