with open("input.txt") as file:
    matrix = [list(line) for line in file.read().splitlines()]

def findXMASInMatrix(matrix):
    numberOfXMAS = 0
    rows = len(matrix)
    columns = len(matrix[0])
    for row in range(rows):
        for col in range(columns):
            XMASCount = searchWord(matrix, row, col)
            if XMASCount != 0:
                numberOfXMAS +=XMASCount
    print(f"Total number of XMAS: {numberOfXMAS}")

def searchWord(matrix, row, col):
    rows = len(matrix)
    columns = len(matrix[0])
    XMASCounter = 0

    if matrix[row][col] != word[0]:
        return False
    print(f"Found {word[0]} at {row},{col}")

    directions = [
        (-1, -1),  # top left
        (-1, 0),  # top middle
        (-1, 1),  # top right
        (0, -1),  # middle left
        (0, 1),  # middle right
        (1, -1),  # bottom left
        (1, 0),  # bottom middle
        (1, 1)  # bottom right
    ]

    for direction in directions:
        dx, dy = direction
        currentX, currentY = row + dx, col + dy
        letterIndex = 1

        while letterIndex<len(word):
            if currentX > rows-1 or currentX <0 or currentY > columns-1 or currentY <0:
                break
            if matrix[currentX][currentY] != word[letterIndex]:
                break
            print(f"Found {word[letterIndex]} at {currentX},{currentY}")
            currentX += dx
            currentY += dy
            letterIndex += 1

        if letterIndex == len(word):
            XMASCounter += 1
    return XMASCounter


word = "XMAS"
findXMASInMatrix(matrix)
