with open("input.txt") as file:
    matrix = [list(line) for line in file.read().splitlines()]

def searchMS(coordsA, matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    XMASCounter = 0

    directions = [
        (-1, -1),  # top left
        (-1, 1),  # top right
        (1, -1),  # bottom left
        (1, 1)  # bottom right
    ]

    for coord in coordsA:
        cross1 = False
        cross2 = False
        dx, dy = directions[0] # top left
        currentX, currentY = coord[0] + dx, coord[1] + dy
        if currentX > rows-1 or currentX <0 or currentY > columns-1 or currentY <0:
            continue
        elif matrix[currentX][currentY] == 'M': # top left is an M
            dx, dy = directions[3]
            currentX, currentY = coord[0] + dx, coord[1] + dy
            if currentX > rows - 1 or currentX < 0 or currentY > columns - 1 or currentY < 0:
                continue
            if matrix[currentX][currentY] == 'S': # bottom right is an S
                cross1 = True
        elif matrix[currentX][currentY] == 'S': # top left is an S
            dx, dy = directions[3]
            currentX, currentY = coord[0] + dx, coord[1] + dy
            if currentX > rows - 1 or currentX < 0 or currentY > columns - 1 or currentY < 0:
                continue
            if matrix[currentX][currentY] == 'M': # bottom right is an M
                cross1 = True

        dx, dy = directions[1] # top right
        currentX, currentY = coord[0] + dx, coord[1] + dy
        if currentX > rows - 1 or currentX < 0 or currentY > columns - 1 or currentY < 0:
            continue
        elif matrix[currentX][currentY] == 'M': # top right is an M
            dx, dy = directions[2]
            currentX, currentY = coord[0] + dx, coord[1] + dy
            if currentX > rows - 1 or currentX < 0 or currentY > columns - 1 or currentY < 0:
                continue
            if matrix[currentX][currentY] == 'S': # bottom left is an S
                cross2 = True
        elif matrix[currentX][currentY] == 'S': # top right is an S
            dx, dy = directions[2]
            currentX, currentY = coord[0] + dx, coord[1] + dy
            if currentX > rows - 1 or currentX < 0 or currentY > columns - 1 or currentY < 0:
                continue
            if matrix[currentX][currentY] == 'M': # bottom left is an M
                cross2 = True
        if cross1 and cross2:
            XMASCounter+=1
    print(f"There are {XMASCounter} XMAS")
    return XMASCounter



def findAInMatrix(matrix):
    coordsA = []
    rows = len(matrix)
    columns = len(matrix[0])
    for row in range(rows):
        for col in range(columns):
            if matrix[row][col] == 'A':
                coordsA.append([row,col])
    searchMS(coordsA, matrix)

findAInMatrix(matrix)
