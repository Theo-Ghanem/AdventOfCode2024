import re
from itertools import product

equations = []

with open("input.txt") as file:
    for line in file:
        parts = line.split(":")
        key = int(parts[0].strip())
        values = list(map(int, parts[1].strip().split()))
        equations.append([key] + values)

def solve_equation(equation):
    operators = ['+', '*']
    combinations = product(operators, repeat = len(equation)-2)
    expected_result = equation[0]
    for combination in combinations:
        expression = str(equation[1])
        for i in range(2, len(equation)):
            expression +=  combination[i-2] + str(equation[i])
            current_result = compute_expression(expression)
            if current_result == expected_result:
                return True
            if current_result > expected_result:
                break
    return False

def compute_expression(expression): # we are ignoring precendence rules
    separated_expression = re.findall(r'\d+|\+|\*', expression)
    result = int(separated_expression[0])
    i = 1
    while i < len(separated_expression):
        operator = separated_expression[i]
        next_number = int(separated_expression[i + 1])
        if operator == '+':
            result += next_number
        elif operator == '*':
            result *= next_number
        i += 2
    return result


count = 0
final_answer = 0
for equation in equations:
    if solve_equation(equation):
        count +=1
        final_answer += equation[0]
        print(f"Equation {equation} is correct, total solved so far: {count}")
print(f"Final answer: {final_answer}")

