with open("input.txt") as file:
    content = file.read().splitlines()

list1 = []
list2 = []
for line in content:
    num1, num2 = line.split()
    list1.append(int(num1))
    list2.append(int(num2))

similarityScore = 0
for i in range(len(list1)):
    numberInList1 = list1[i]
    counter =0
    for j in range(len(list2)):
        if numberInList1 == list2[j]:
            counter +=1
    similarityScore += numberInList1 * counter
print(similarityScore)



