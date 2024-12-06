with open("input.txt") as file:
    content = file.read().splitlines()

# Find the index of the empty line
empty_line_index = content.index('')

# Split the content into two sections
pageOrderingRules = content[:empty_line_index]
updates = content[empty_line_index + 1:]

pageOrderingRulesList = []
for rule in pageOrderingRules:
    numbers = rule.split('|')
    pageOrderingRulesList.append((int(numbers[0]), int(numbers[1])))

updatesList = [list(map(int, update.split(','))) for update in updates]

def check_update(update):

    update_is_correct = True
    for number in update:
        rules_for_update = []
        for rule in pageOrderingRulesList:
            if number in rule: #check if the rule applies to this number
                rules_for_update.append(rule)
                # print(rules_for_update)
        for rule in rules_for_update:
            index_number = update.index(number)
            if rule[0] == number: # number is in first spot so must be before
                # print(f"{number} is in the first spot of the tuple {rule}")
                if rule[1] in update: # check that the other number is in the update, if not ignore
                    index_other_number = update.index(rule[1])
                    if index_other_number < index_number:
                        update_is_correct = False
            elif rule[1] == number: # number if in second spot so must be after
                # print(f"{number} is in the second spot of the tuple {rule}")
                if rule[0] in update: # check that the other number is in the update, if not ignore
                    index_other_number = update.index(rule[0])
                    if index_number < index_other_number:
                        update_is_correct = False
    print("update is correct: ", update_is_correct)
    return update_is_correct


def get_middle_value(update):
    middle_index = len(update)//2
    middle_value = update[middle_index]
    return middle_value


correct_updates = []
for update in updatesList:
    is_correct = check_update(update)
    if is_correct:
        correct_updates.append(update)

result = 0
for correct_update in correct_updates:
    result += get_middle_value(correct_update)
print("result: ", result)


