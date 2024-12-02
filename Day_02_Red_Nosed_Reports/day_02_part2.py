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
        safeReports += 1
    else :
        for i in range (len(report)):
            tmpReport = report.copy()
            del(tmpReport[i])
            if ((isDecreasing(tmpReport) or isIncreasing(tmpReport)) and checkGap(tmpReport)):
                safeReports += 1
                break
print(safeReports)
