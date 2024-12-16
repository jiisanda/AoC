def check_correct_order(rules, update):
    for r in rules:
        if r[0] in update and r[1] in update:
            if update.index(r[0]) > update.index(r[1]):
                return True
    return False


def get_sum_of_correct_order(rules, updates):
    correct_updates = [update for update in updates if not check_correct_order(rules, update)]
    print(f"correct_updates: {correct_updates}")
    result = 0
    for order in correct_updates:
        result += order[len(order) // 2]

    return result


if __name__ == '__main__':
    rules = []
    updates = []
    with open('test_input.txt') as file:
        content = file.read().split('\n')
        for line in content:
            if '|' in line:
                rule = list(map(int, line.split('|')))
                rules.append(rule)
            elif ',' in line:
                update = list(map(int, line.split(',')))
                updates.append(update)

    print(f"rules: {rules}")
    print(f"updates: {updates}")

    print(f"answer = {get_sum_of_correct_order(rules, updates)}")
