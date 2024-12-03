import re

with open("input.txt") as file:
    content = file.read().splitlines()

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
matches = []
for line in content:
    matches.extend(re.findall(pattern, line))
print(matches)

result = 0
for mul in matches:
    int1 = int(mul[0])
    int2 = int(mul[1])
    result += int1 * int2
print(result)