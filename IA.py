from collections import deque

class Board:
  def __init__(self,matrix):
    self.matrix = matrix

# TODO: delete this class if not used
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

def goUp(board,x_axis,y_axis):
    #print('case 0')
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
    #print('case 2')

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
    #print('case 3')
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

# breadth first algorithm
def breadthFirst(matrix):
    found = False
    #list
    visited = []
    #queue
    #queue = deque([matrix])
    queue = deque()
    queue.append(matrix)
    counter = 0
    #While queue has contents
    while queue and not found:
        #print("queue: " + str(queue))
        node = queue.popleft()
        counter = counter + 1
        if node not in visited:
            #print("Actual node: " + str(node))
            # check if the node is the solution
            if isSolved(node):
                # empty the queue
                print("Actual node: " + str(node))
                print("puzzle solved")
                print("After " + str(counter) + " iterations")
                queue.clear()
                found = True

            add_to_visited(node, visited)

            if not found:
                # found = isSolved(node)
                up,right,down,left = allMoves(node)
                x_axis, y_axis = findZero(node)

                if up:
                    newNode = goUp(node, x_axis, y_axis)
                    #print("newNode: " + str(newNode))
                    if newNode not in visited:
                        #print("up")
                        queue.append(newNode)
                    
                    # delete newNode
                    newNode = None

                        #print("initial node: " + str(node))

                if right:
                    newNode = goRight(node, x_axis, y_axis)
                    #print("newNode: " + str(newNode))
                    if newNode not in visited:
                        #print("right")
                        queue.append(newNode)
                    
                    # delete newNode
                    newNode = None

                        # queue.append(newNode)
                    # queue.append(newNode)

                if down:
                    newNode = goDown(node, x_axis, y_axis)
                    #print("newNode: " + str(newNode))
                    if newNode not in visited:
                        #print("down")
                        queue.append(newNode)
                    
                    # delete newNode
                    newNode = None

                        # queue.append(newNode)
                    # queue.append(newNode)

                if left:
                    newNode = goLeft(node, x_axis, y_axis)
                    #print("newNode: " + str(newNode))
                    if newNode not in visited:
                        #print("left")
                        queue.append(newNode)
                    
                    # delete newNode
                    newNode = None

                        # queue.append(newNode)
                    # queue.append(newNode)

def matrixRating(matrix):
    rating = 0
    x = 0
    y = 0
    coordinates_solved = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)] 
    for i in range(3):
        for j in range(3):
            value = matrix[j][i]
            print(value)
            x = coordinates_solved[value-1][0] + j
            y = coordinates_solved[value-1][1] + i
            rating = rating + x + y
    
    return rating

def calculate_heuristic_value(matrix):
    # the heuristic value is the sum of the manhattan distances of each number to its correct position
    heuristic = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] != 0:
                x_axis = (matrix[i][j] - 1) % 3
                y_axis = (matrix[i][j] - 1) // 3
                heuristic = heuristic + abs(x_axis - j) + abs(y_axis - i)
    return heuristic

# greedy algorithm uses the same logic as the breadth first algorithm but additionally
# uses a heuristic to find the solution
def greedy(matrix):
    found = False
    #list
    visited = []
    #queue
    #queue = deque([matrix])
    queue = deque()
    queue.append(matrix)
    counter = 0
    #While queue has contents
    while queue and not found:
        #print("queue: " + str(queue))
        node = queue.popleft()
        counter = counter + 1
        if node not in visited:
            #print("Actual node: " + str(node))
            # check if the node is the solution
            if isSolved(node):
                # empty the queue
                print("Actual node: " + str(node))
                print("puzzle solved")
                print("After " + str(counter) + " iterations")
                queue.clear()
                found = True

            add_to_visited(node, visited)

            # all 4 possible moves will be checked and only the one with the lowest heuristic value will be added to the queue
            if not found:
                # found = isSolved(node)
                up,right,down,left = allMoves(node)
                x_axis, y_axis = findZero(node)
                
                # we use a vector of 4 elements to store the heuristic values of the 4 possible moves
                # the heuristic value of a move is -1 if the move is not possible
                heuristic_values = [-1, -1, -1, -1]

                if up:
                    newNode = goUp(node, x_axis, y_axis)
                    #print("newNode: " + str(newNode))
                    if newNode not in visited:
                        #print("up")
                        # queue.append(newNode)
                    
                        # delete newNode
                        heuristic_values[0] = calculate_heuristic_value(newNode)
                    newNode = None

                        #print("initial node: " + str(node))

                if right:
                    newNode = goRight(node, x_axis, y_axis)
                    #print("newNode: " + str(newNode))
                    if newNode not in visited:
                        #print("right")
                        # queue.append(newNode)
                    
                        heuristic_values[1] = calculate_heuristic_value(newNode)
                    # delete newNode
                    newNode = None

                        # queue.append(newNode)
                    # queue.append(newNode)

                if down:
                    newNode = goDown(node, x_axis, y_axis)
                    #print("newNode: " + str(newNode))
                    if newNode not in visited:
                        #print("down")
                        #queue.append(newNode)
                        heuristic_values[2] = calculate_heuristic_value(newNode)
                    # delete newNode
                    newNode = None

                        # queue.append(newNode)
                    # queue.append(newNode)

                if left:
                    newNode = goLeft(node, x_axis, y_axis)
                    #print("newNode: " + str(newNode))
                    if newNode not in visited:
                        #print("left")
                        # queue.append(newNode)

                        heuristic_values[3] = calculate_heuristic_value(newNode)
                    
                    # delete newNode
                    newNode = None

                # find the move with the lowest heuristic value
                min_heuristic = 0

                # find the first move that is possible
                for i in range(4):
                    if heuristic_values[i] != -1:
                        min_heuristic = i
                        break

                # find the move with the lowest heuristic value
                for i in range(4):
                    if heuristic_values[i] != -1:
                        if heuristic_values[i] < heuristic_values[min_heuristic]:
                            min_heuristic = i
                
                # add the move with the lowest heuristic value to the queue
                # there is no need to check if the move is possible because it has already been checked
                if min_heuristic == 0:
                    newNode = goUp(node, x_axis, y_axis)
                    queue.append(newNode)
                if min_heuristic == 1:
                    newNode = goRight(node, x_axis, y_axis)
                    queue.append(newNode)
                if min_heuristic == 2:
                    newNode = goDown(node, x_axis, y_axis)
                    queue.append(newNode)
                if min_heuristic == 3:
                    newNode = goLeft(node, x_axis, y_axis)
                    queue.append(newNode)

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

def generate_sons(matrix):
    matrixToVisit = []

    up,right,down,left = allMoves(matrix)
    x_axis, y_axis = findZero(matrix)

    if up:
        newMatrix = goUp(matrix, x_axis, y_axis)
        matrixToVisit.append(newMatrix)

    if right:
        newMatrix = goRight(matrix, x_axis, y_axis)
        matrixToVisit.append(newMatrix)

    if down:
        newMatrix = goDown(matrix, x_axis, y_axis)
        matrixToVisit.append(newMatrix)
    if left:
        newMatrix = goLeft(matrix, x_axis, y_axis)
        matrixToVisit.append(newMatrix)

    return matrixToVisit

def IDS(matrix):
    global visited
    visited = []
    
    
    depth_goal = 0
    found = False
    while not found:
        result_given_level = IDSRecursive(matrix, depth_goal)
        if result_given_level is not None:
            print("Actual node: " + str(matrix))
            print("puzzle solved")
            found = True
        depth_goal = depth_goal + 1

def IDSRecursive(matrix, level):   
    if isSolved(matrix):                
            return matrix
    # TODO: change to elif ?
    if level == 0:
        # base case of the recursion, just return None because answer not found
        return None
    else:
        sons = generate_sons(matrix)
        for son in sons:
            if son not in visited:
                visited.append(son)
                answer = IDSRecursive(son, level-1)
                if answer is not None:
                    print("siuuuuuu")
                    return answer
                
        # TODO: change to eelse ?
        # calculate all posible sons of the current matrix
        # TODO: use function specially to create sons ?
        # TODO: hwo about the visited node ? need to don't cycle ad vita eternam
        # for each available son call the IDSRecursive function