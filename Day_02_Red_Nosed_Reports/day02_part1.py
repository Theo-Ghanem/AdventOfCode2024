with open("input.txt") as file:
    content = file.read().splitlines()

def isDecreasing(report):
    for level in range (len(report)-1):
        if report[level] <= report[level+1]:
            return False
    return True

def isIncreasing(report):
    for level in range (len(report)-1):
        if report[level] >= report[level+1]:
            return False
    return True


def checkGap(report):
    for level in range (len(report)-1):
        gap = abs(report[level] - report[level + 1])
        if gap <1 or gap>3:
            return False
    return True

safeReports = 0
for report in content:
    report = list(map(int, report.split()))
    if ((isDecreasing(report) or isIncreasing(report)) and checkGap(report)):
        print(report)
        safeReports += 1
print(safeReports)
