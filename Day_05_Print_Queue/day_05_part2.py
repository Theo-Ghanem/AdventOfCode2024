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

def switch_with_right(list, index):
    if index < len(list) - 1:
        list[index], list[index + 1] = list[index + 1], list[index]
    return list

def switch_with_left(list, index):
    if index > 0:
        list[index], list[index - 1] = list[index - 1], list[index]
    return list

def switch_numbers(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]
    return list

def check_update_with_corrections(update):
    update_is_correct = True
    for number in update:
        rules_for_update = []
        for rule in pageOrderingRulesList :
            if number in rule and (rule[0] in update or rule[1] in update): #check if the rule applies to this number and that the other number is in the update, if not ignore
                rules_for_update.append(rule)
        for rule in rules_for_update:
            index_number = update.index(number)
            if rule[0] == number: # number is in first spot so must be before
                if rule[1] in update: # check that the other number is in the update, if not ignore
                    index_other_number = update.index(rule[1])
                    if index_other_number < index_number:
                        print(f"{update} is incorrect")
                        update_is_correct = False
                        updated_update = switch_numbers(update,index_number,index_other_number)
                        print(f"Switching {number} and {rule[1]}")
                        check_update_with_corrections(updated_update)

            elif rule[1] == number: # number if in second spot so must be after
                if rule[0] in update: # check that the other number is in the update, if not ignore
                    index_other_number = update.index(rule[0])
                    if index_number < index_other_number:
                        print(f"{update} is incorrect")
                        update_is_correct = False
                        updated_update = switch_numbers(update,index_number,index_other_number)
                        print(f"Switching {number} and {rule[0]}")
                        check_update_with_corrections(updated_update)
    if update_is_correct:
        print(f"Update: {update} is correct: ")
    return update

def check_update_without_correction(update):
    update_is_correct = True
    for number in update:
        rules_for_update = []
        for rule in pageOrderingRulesList:
            if number in rule: #check if the rule applies to this number
                rules_for_update.append(rule)
        for rule in rules_for_update:
            index_number = update.index(number)
            if rule[0] == number: # number is in first spot so must be before
                if rule[1] in update: # check that the other number is in the update, if not ignore
                    index_other_number = update.index(rule[1])
                    if index_other_number < index_number:
                        update_is_correct = False
            elif rule[1] == number: # number if in second spot so must be after
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
for update2 in updatesList:
    is_correct = check_update_without_correction(update2)
    if is_correct:
        correct_updates.append(update2)

result_correct = 0
for correct_update2 in correct_updates:
    result_correct += get_middle_value(correct_update2)

all_updates = []
for update in updatesList:
    retrieved_update = check_update_with_corrections(update)
    if retrieved_update != None:
        all_updates.append(check_update_with_corrections(update))

result = 0
for correct_update in all_updates:
    print(f" Adding {get_middle_value(correct_update)}")
    result += get_middle_value(correct_update)

print("Result without corrections: ", result_correct)
print("result with corrections: ", result)
print("final result: ", result-result_correct)