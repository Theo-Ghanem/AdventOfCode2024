with open("input.txt") as file:
    content = file.read().splitlines()

list1 = []
list2 = []
for line in content:
    num1, num2 = line.split()
    list1.append(int(num1))
    list2.append(int(num2))

list1.sort()
list2.sort()
distance = 0
for i in range(len(list1)):
    distance += abs(list1[i]-list2[i])
print (distance)



