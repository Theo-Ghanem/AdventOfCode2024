import re

with open("input.txt") as file:
    content = file.read().splitlines()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(?P<do>do\(\))|(?P<dont>don't\(\))"
matches = []
for line in content:
    matches.extend(re.findall(pattern, line))
print(matches)

result = 0
do = True
for mul in matches:
    print("Checking ", mul)
    if (mul[0] and mul[1] and do):
        int1 = int(mul[0])
        int2 = int(mul[1])
        result += int1 * int2
        print(f"Adding: {int1} * {int2}")
    elif (mul[2]):
        do = True
        print("setting do to true")
    else:
        do = False
        print("setting do to false")


print(result)