def check_correct_order(rules, update):
    for r in rules:
        if r[0] in update and r[1] in update:
            if update.index(r[0]) > update.index(r[1]):
                return True
    return False


def arrange_update_as_rules(rules, update):
    arranged = update.copy()
    n = len(arranged)
    swapped = True

    while swapped:
        swapped = False
        for num1, num2 in rules:
            if num1 in arranged and num2 in arranged:
                x = arranged.index(num1)
                y = arranged.index(num2)
                if x > y:
                    arranged[x], arranged[y] = arranged[y], arranged[x]
                    swapped = True

    return arranged


def get_sum_of_middle_corrected_order(rules, updates):
    incorrect_updates = [update for update in updates if check_correct_order(rules, update)]
    print(f"incorrect_updates: {incorrect_updates}")

    result = 0
    for update in incorrect_updates:
        corrected_updates = arrange_update_as_rules(rules, update)
        print(f"corrected_updates: {corrected_updates}")
        result += corrected_updates[len(corrected_updates) // 2]

    return result

if __name__ == '__main__':
    rules = []
    updates = []
    with open('day5_input.txt') as file:
        content = file.read().split('\n')
        for line in content:
            if '|' in line:
                rule = list(map(int, line.split('|')))
                rules.append(rule)
            elif ',' in line:
                update = list(map(int, line.split(',')))
                updates.append(update)
    #
    # print(f"rules: {rules}")
    # print(f"updates: {updates}")

    print(f"answer = {get_sum_of_middle_corrected_order(rules, updates)}")
