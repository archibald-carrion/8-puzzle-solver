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

def goUp(board,y_axis,x_axis):
    print('case 0')
    #Create a new matrix
    matrix = board.copy()
    temp_value = matrix[y_axis-1][x_axis]
    matrix[y_axis-1][x_axis] = 0
    matrix[y_axis][x_axis] = temp_value
    return matrix

def goRight(board,y_axis,x_axis):
    print('case 1')
    #Create a new matrix
    matrix = board.copy()
    temp_value = matrix[y_axis][x_axis+1]
    matrix[y_axis][x_axis+1] = 0
    matrix[y_axis][x_axis] = temp_value
    return matrix

def goDown(board,y_axis,x_axis):
    print('case 2')
    #Create a new matrix
    matrix = board.copy()
    temp_value = matrix[y_axis+1][x_axis]
    matrix[y_axis+1][x_axis] = 0
    matrix[y_axis][x_axis] = temp_value
    return matrix

def goLeft(board,y_axis,x_axis):
    print('case 3')
    #Create a new matrix
    matrix = board.copy()
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
            [4, 0, 5],
            [6, 7, 8]]
    if board == solved:
        same = True
    return same

def widthFirst():
    found = False
    matrix = matrix_solvable
    #Iteration for each level
    while not(found):
        found = isSolved(matrix)
        up,right,down,left = allMoves(matrix)
        nextLevel = []
        if up:
            newMatrix = goUp(matrix)
            nextLevel.append(newMatrix)
        if right:
            newMatrix = goRight(matrix)
            nextLevel.append(newMatrix)
        if down:
            newMatrix = goDown(matrix)
            nextLevel.append(newMatrix)
        if left:
            newMatrix = goLeft(matrix)
            nextLevel.append(newMatrix)


def breadthFirst(graph, start):
    #list
    visited = set()
    #queue
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)

            print(node)  # Do something with the node

            
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)





print(matrix_solvable)
tryMove()
print(matrix_solvable)