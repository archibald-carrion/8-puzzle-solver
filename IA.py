from collections import deque

matrix_solvable = [[1, 4, 3],
                   [7, 6, 5],
                   [8, 2, 0]]

class Board:
  def __init__(self,matrix):
    self.matrix = matrix


class Movement:
  def __init__(self, state, pastMove, level):
    self.state = state
    self.pastMove = pastMove
    self.level = level


# find the zero in the matrix
def findZero(board):
    matrix = board
    x_axis, y_axis = 0, 0
    found = False
    while not(found) and y_axis < 3:
        x_axis = 0
        while not(found) and x_axis < 3:
            if matrix[y_axis][x_axis] == 0:
                found = True
            else:
                x_axis = x_axis + 1
        if not(found):
            y_axis = y_axis + 1
        
    
    return x_axis, y_axis

# try to move the zero to adjacent position
def tryMove():
    #find zero
    x_axis, y_axis = findZero(matrix_solvable)
    
    # 0 states
    print(x_axis, y_axis)

    can_go_up = (y_axis > 0)
    can_go_right = (x_axis < 2)
    can_go_down = (y_axis < 2)
    can_go_left = (x_axis > 0)
    
    if can_go_up:
       print('case 0')
       print(matrix_solvable[y_axis][x_axis])

       temp_value = matrix_solvable[y_axis-1][x_axis]
       matrix_solvable[y_axis-1][x_axis] = 0
       print(matrix_solvable[y_axis][x_axis])
       matrix_solvable[y_axis][x_axis] = temp_value

    elif (can_go_right):
       print('case 1')
       temp_value = matrix_solvable[y_axis][x_axis+1]
       matrix_solvable[y_axis][x_axis+1] = 0
       matrix_solvable[y_axis][x_axis] = temp_value

    elif(can_go_down):
       print('case 2')
       temp_value = matrix_solvable[y_axis+1][x_axis]
       matrix_solvable[y_axis+1][x_axis] = 0
       matrix_solvable[y_axis][x_axis] = temp_value

    elif (can_go_left):
       print('case 3')
       temp_value = matrix_solvable[y_axis][x_axis-1]
       matrix_solvable[y_axis][x_axis-1] = 0
       matrix_solvable[y_axis][x_axis] = temp_value

def goUp(board,x_axis,y_axis):
    print('case 0')
    #Create a new matrix

    matrix = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            matrix[i][j] = board[i][j]
    
    #matrix = board.copy()
    temp_value = matrix[y_axis-1][x_axis]
    matrix[y_axis-1][x_axis] = 0
    matrix[y_axis][x_axis] = temp_value
    return matrix

def goRight(board,x_axis,y_axis):
    print('case 1')

    matrix = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            matrix[i][j] = board[i][j]
    #Create a new matrix
    #matrix = board.copy()
    temp_value = matrix[y_axis][x_axis+1]
    matrix[y_axis][x_axis+1] = 0
    matrix[y_axis][x_axis] = temp_value
    return matrix

def goDown(board,x_axis,y_axis):
    print('case 2')

    matrix = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            matrix[i][j] = board[i][j]
    #Create a new matrix
    #matrix = board.copy()

    temp_value = matrix[y_axis+1][x_axis]
    matrix[y_axis+1][x_axis] = 0
    matrix[y_axis][x_axis] = temp_value
    return matrix

def goLeft(board,x_axis,y_axis):
    matrix = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            matrix[i][j] = board[i][j]
    print('case 3')
    #Create a new matrix
    #matrix = board.copy()
    temp_value = matrix[y_axis][x_axis-1]
    matrix[y_axis][x_axis-1] = 0
    matrix[y_axis][x_axis] = temp_value
    return matrix

def allMoves(board):
    x_axis, y_axis = findZero(board)
    can_go_up = (y_axis > 0)
    can_go_right = (x_axis < 2)
    can_go_down = (y_axis < 2)
    can_go_left = (x_axis > 0)
    return can_go_up, can_go_right, can_go_down , can_go_left

def isSolved(board):
    same = False
    solved = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]
    if board == solved:
        same = True
    return same

# def widthFirst():
#     found = False
#     matrix = matrix_solvable
#     #Iteration for each level
#     while not(found):
#         found = isSolved(matrix)
#         up,right,down,left = allMoves(matrix)
#         nextLevel = []
#         if up:
#             newNode = goUp(matrix)
#             nextLevel.append(newNode)
#         if right:
#             newNode = goRight(matrix)
#             nextLevel.append(newNode)
#         if down:
#             newNode = goDown(matrix)
#             nextLevel.append(newNode)
#         if left:
#             newNode = goLeft(matrix)
#             nextLevel.append(newNode)

# Function to check if the matrix is currently in the visited set
def is_matrix_visited(matrix, visited):
    for visited_node in visited:
        matrix_is_visited = True
        for i in range(3):
            for j in range(3):
                if visited_node[i][j] != matrix[i][j]:
                    matrix_is_visited = False
        if matrix_is_visited:
            return True
    return False


def add_to_visited(matrix, visited):
    # create a matrix with 3 rows and 3 columns
    matrix_copy = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            matrix_copy[i][j] = matrix[i][j]
            
    visited.append(matrix_copy)


def breadthFirst(matrix):
    found = False
    #list
    visited = []
    #queue
    #queue = deque([matrix])
    queue = deque()
    queue.append(matrix)
    #While queue has contents
    while queue and not found:
        print("queue: " + str(queue))
        node = queue.popleft()

        if node not in visited:
            print("Actual node: " + str(node))
            # check if the node is the solution
            if isSolved(node):
                # empty the queue
                print("puzzle solved")
                queue.clear()
                found = True

            add_to_visited(node, visited)

            if not found:
                # found = isSolved(node)
                up,right,down,left = allMoves(node)
                x_axis, y_axis = findZero(node)

                if up:
                    newNode = goUp(node, x_axis, y_axis)
                    print("newNode: " + str(newNode))
                    if newNode not in visited:
                        print("up")
                        queue.append(newNode)
                    
                    # delete newNode
                    newNode = None

                        #print("initial node: " + str(node))

                if right:
                    newNode = goRight(node, x_axis, y_axis)
                    print("newNode: " + str(newNode))
                    if newNode not in visited:
                        print("right")
                        queue.append(newNode)
                    
                    # delete newNode
                    newNode = None

                        # queue.append(newNode)
                    # queue.append(newNode)

                if down:
                    newNode = goDown(node, x_axis, y_axis)
                    print("newNode: " + str(newNode))
                    if newNode not in visited:
                        print("down")
                        queue.append(newNode)
                    
                    # delete newNode
                    newNode = None

                        # queue.append(newNode)
                    # queue.append(newNode)

                if left:
                    newNode = goLeft(node, x_axis, y_axis)
                    print("newNode: " + str(newNode))
                    if newNode not in visited:
                        print("left")
                        queue.append(newNode)
                    
                    # delete newNode
                    newNode = None

                        # queue.append(newNode)
                    # queue.append(newNode)


# Function to check if the matrix is solvable
# a matrix is solvable if the number of inversions is even
# an inversion is when a number is greater than another number that is after it
# 0 is not counted as a number in this case, only the numbers from 1 to 8
# TODO: check if this is correct
def isTableSolvable(matrix):
    #Count the number of inversions
    inversions = 0
    #Create a list with the matrix
    list_matrix = []
    for i in range(3):
        for j in range(3):
            list_matrix.append(matrix[i][j])
    #Count the number of inversions
    for i in range(9):
        for j in range(i+1,9):
            if list_matrix[i] > list_matrix[j] and list_matrix[i] != 0 and list_matrix[j] != 0:
                inversions = inversions + 1
    #If the number of inversions is odd, the matrix is not solvable
    if inversions % 2 != 0:
        return False
    return True