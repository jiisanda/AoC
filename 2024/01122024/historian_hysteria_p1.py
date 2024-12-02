from typing import List


def get_diff_list_s_sum(l1: List[int], l2: List[int]) -> int:
    result = []
    l1, l2 = sorted(l1), sorted(l2)
    for i in range(len(l1)):
        result.append(abs(l1[i] - l2[i]))

    return sum(result)


if __name__ == '__main__':
    list1, list2 = [], []
    with open('2024/01122024/day1_input.txt') as file:
        for line in file:
            a, b = line.split()
            list1.append(int(a))
            list2.append(int(b))

    # print(list1, list2)
    diff_list = get_diff_list_s_sum(list1, list2)
    print(diff_list)
