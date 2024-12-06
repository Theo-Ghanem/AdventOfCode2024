with open("input.txt") as file:
    matrix = [list(line) for line in file.read().splitlines()]

def print_matrix(matrix):
    for row in matrix:
        print(row)

def find_guard(matrix):
    rows = len(matrix)-1
    columns = len(matrix[0])-1
    for row in range(rows):
        for col in range(columns):
            if matrix[row][col] == '^':
                return [row,col]


def move_guard(matrix):
    guard_location = find_guard(matrix)
    has_left = False
    while not has_left:
        matrix, guard_location, has_left = move_up(matrix, guard_location)
        if has_left:
            break
        matrix, guard_location, has_left = move_right(matrix, guard_location)
        if has_left:
            break
        matrix, guard_location, has_left = move_down(matrix, guard_location)
        if has_left:
            break
        matrix, guard_location, has_left = move_left(matrix, guard_location)
        if has_left:
            break
    return matrix

def count_positions(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    count = 0
    for row in range(rows):
        for col in range(columns):
            if matrix[row][col] == 'X':
                count += 1
                # matrix[row][col] = 'O'
    print(f"There are {count} distinct positions")
    # print_matrix(matrix)
    return(count)

def move_up(matrix, guard_location):
    print(f"Guard {[guard_location[0], guard_location[1]]}")
    print(f"Up 1 {[guard_location[0]-1, guard_location[1]]}")
    while guard_location[0] - 1 >= 0 and matrix[guard_location[0] - 1][guard_location[1]] != '#':
        matrix[guard_location[0]][guard_location[1]], matrix[guard_location[0]-1][guard_location[1]] = 'X',matrix[guard_location[0]][guard_location[1]]
        # print(f"Guard is now at  {find_guard(matrix)}")
        # print_matrix(matrix)
        guard_location = [guard_location[0]-1, guard_location[1]]
    matrix[guard_location[0]][guard_location[1]] = '>'
    has_left = False
    if guard_location[0] == 0: # Guard is at top and will leave route
        matrix[guard_location[0]][guard_location[1]] = 'X'
        has_left = True
        print("Left route through top:")
    else:
        print("Turning right")
    # print_matrix(matrix)
    return matrix, guard_location, has_left

def move_right(matrix, guard_location):
    print(f"Guard {[guard_location[0], guard_location[1]]}")
    print(f"Up 1 {[guard_location[0]-1, guard_location[1]]}")
    while guard_location[1] + 1 < len(matrix[0]) and matrix[guard_location[0]][guard_location[1]+1] != '#':
        matrix[guard_location[0]][guard_location[1]], matrix[guard_location[0]][guard_location[1]+1] = 'X',matrix[guard_location[0]][guard_location[1]]
        # print(f"Guard is now at  {find_guard(matrix)}")
        # print_matrix(matrix)
        guard_location = [guard_location[0], guard_location[1]+1]
    matrix[guard_location[0]][guard_location[1]] = 'v'
    has_left = False
    if guard_location[1] == (len(matrix[0])-1): # Guard is on the right wall and will leave route
        has_left = True
        matrix[guard_location[0]][guard_location[1]] = 'X'
        print("Left route through right:")
    else:
        print("Turning down:")
    # print_matrix(matrix)

    return matrix, guard_location, has_left

def move_down(matrix, guard_location):
    print(f"Guard {[guard_location[0], guard_location[1]]}")
    print(f"Down 1 {[guard_location[0]+1, guard_location[1]]}")
    while guard_location[0] + 1 < len(matrix) and matrix[guard_location[0] + 1][guard_location[1]] != '#':
        matrix[guard_location[0]][guard_location[1]], matrix[guard_location[0]+1][guard_location[1]] = 'X',matrix[guard_location[0]][guard_location[1]]
        # print(f"Guard is now at  {find_guard(matrix)}")
        # print_matrix(matrix)
        guard_location = [guard_location[0]+1, guard_location[1]]
    matrix[guard_location[0]][guard_location[1]] = '<'
    has_left = False
    if guard_location[0] == (len(matrix)-1): # Guard is on bottom wall and will leave route
        has_left = True
        matrix[guard_location[0]][guard_location[1]] = 'X'
        print("Left route through bottom:")
    else:
        print("Turning left:")
    # print_matrix(matrix)
    return matrix, guard_location, has_left

def move_left(matrix, guard_location):
    print(f"Guard {[guard_location[0], guard_location[1]]}")
    print(f"Up 1 {[guard_location[0], guard_location[1]-1]}")
    while guard_location[1] - 1 >= 0 and matrix[guard_location[0]][guard_location[1]-1] != '#':
        matrix[guard_location[0]][guard_location[1]], matrix[guard_location[0]][guard_location[1]-1] = 'X',matrix[guard_location[0]][guard_location[1]]
        # print(f"Guard is now at  {find_guard(matrix)}")
        # print_matrix(matrix)
        guard_location = [guard_location[0], guard_location[1]-1]
    matrix[guard_location[0]][guard_location[1]] = '^'
    has_left = False
    if guard_location[1] == 0: # Guard is on left wall and will leave route
        has_left = True
        matrix[guard_location[0]][guard_location[1]] = 'X'
        print("Left route through left:")
    else:
        print("Turning up:")
    # print_matrix(matrix)

    return matrix, guard_location, has_left


matrix = move_guard(matrix)
count_positions(matrix)
