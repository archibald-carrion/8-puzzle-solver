from collections import deque

# visited is a global variable that will store all the visited nodes
# it is used in the IDS algorithm to check if a node has already been visited
visited = []

# find the zero in the matrix
def findZero(matrix):
    xAxis, yAxis = 0, 0
    found = False
    while not(found) and yAxis < 3:
        xAxis = 0
        while not(found) and xAxis < 3:
            if matrix[yAxis][xAxis] == 0:
                found = True
            else:
                xAxis = xAxis + 1
        if not(found):
            yAxis = yAxis + 1
        
    return xAxis, yAxis

# goUp function moves the zero up
# returns the new matrix
def goUp(matrix,xAxis,yAxis):
    # Create a new newMatrix
    newMatrix = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            newMatrix[i][j] = matrix[i][j]
    
    tempValue = newMatrix[yAxis-1][xAxis]
    newMatrix[yAxis-1][xAxis] = 0
    newMatrix[yAxis][xAxis] = tempValue
    return newMatrix

# goRight function moves the zero right
# returns the new matrix
def goRight(matrix,xAxis,yAxis):
    # Create a new matrix
    newMatrix = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            newMatrix[i][j] = matrix[i][j]

    tempValue = newMatrix[yAxis][xAxis+1]
    newMatrix[yAxis][xAxis+1] = 0
    newMatrix[yAxis][xAxis] = tempValue
    return newMatrix

# goDown function moves the zero down
# returns the new matrix
def goDown(matrix,xAxis,yAxis):
    # Create a new matrix
    newMatrix = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            newMatrix[i][j] = matrix[i][j]

    tempValue = newMatrix[yAxis+1][xAxis]
    newMatrix[yAxis+1][xAxis] = 0
    newMatrix[yAxis][xAxis] = tempValue
    return newMatrix

# goLeft function moves the zero left
# returns the new matrix
def goLeft(matrix,xAxis,yAxis):
    # Create a new matrix
    newMatrix = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            newMatrix[i][j] = matrix[i][j]

    tempValue = newMatrix[yAxis][xAxis-1]
    newMatrix[yAxis][xAxis-1] = 0
    newMatrix[yAxis][xAxis] = tempValue
    return newMatrix

# allMoves function returns a tuple with 4 boolean values, each value is True
# if the zero can move in that direction
def allMoves(board):
    xAxis, yAxis = findZero(board)
    canGoUp = (yAxis > 0)
    canGoRight = (xAxis < 2)
    canGoDown = (yAxis < 2)
    canGoLeft = (xAxis > 0)
    return canGoUp, canGoRight, canGoDown , canGoLeft

# isSolved function checks if the matrix is the solved matrix, the goal matrix
# is harcoded in the function as [[1, 2, 3],[4, 5, 6],[7, 8, 0]]
def isSolved(board):
    same = False
    solved = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]
    if board == solved:
        same = True
    return same

# TODO: delete this function if it is not used
# # is_matrix_visited function checks if a matrix has already been visited
# def is_matrix_visited(matrix, visited):
#     for visited_node in visited:
#         matrix_is_visited = True
#         for i in range(3):
#             for j in range(3):
#                 if visited_node[i][j] != matrix[i][j]:
#                     matrix_is_visited = False
#         if matrix_is_visited:
#             return True
#     return False

# addToVisited function adds a matrix to the visited list
def addToVisited(matrix, visited):
    # create a matrix with 3 rows and 3 columns
    matrixCopy = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            matrixCopy[i][j] = matrix[i][j]
            
    visited.append(matrixCopy)

# breadthFirst function uses the breadth first algorithm to solve the puzzle
def breadthFirst(matrix):
    found = False
    visited = [] # list
    queue = deque()
    queue.append(matrix)
    counter = 0  # used to check the # of iterations, only for testingpurposes

    # while the queue is not empty and the solution has not been found
    while queue and not found:
        node = queue.popleft() # get the first element of the queue
        counter = counter + 1
        # TODO: following condition might not be necessary as the visited list 
        # is checked before adding a node to the queue
        if node not in visited:
            # check if the node is the solution
            if isSolved(node):
                # TODO: do not print following lines in the final version for
                # time performance
                # print("Actual node: " + str(node))
                # print("puzzle solved")
                # print("After " + str(counter) + " iterations")
                queue.clear() # empty the queue
                found = True

            addToVisited(node, visited)

            if not found:
                # check all 4 possible moves and add them to the queue if they
                # have not been visited and are possible
                up,right,down,left = allMoves(node)
                xAxis, yAxis = findZero(node)
                
                if up:
                    newNode = goUp(node, xAxis, yAxis)
                    if newNode not in visited:
                        queue.append(newNode)
                    newNode = None

                if right:
                    newNode = goRight(node, xAxis, yAxis)
                    if newNode not in visited:
                        queue.append(newNode)
                    newNode = None

                if down:
                    newNode = goDown(node, xAxis, yAxis)
                    if newNode not in visited:
                        queue.append(newNode)
                    newNode = None

                if left:
                    newNode = goLeft(node, xAxis, yAxis)
                    if newNode not in visited:
                        queue.append(newNode)
                    newNode = None

# calculateHeuristicValue function calculates the heuristic value of a matrix
# the heuristic value is the sum of the manhattan distances of each number to
# its correct position in an hipothetical "empty" matrix
def calculateHeuristicValue(matrix):
    heuristic = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] != 0:
                xAxis = (matrix[i][j] - 1) % 3
                yAxis = (matrix[i][j] - 1) // 3
                # abs(xAxis-j) + abs(yAxis-i) is the n_th manhattan distance
                heuristic = heuristic + abs(xAxis - j) + abs(yAxis - i)
    return heuristic

# matrixRating is not used in the final version of the app, because it
# resolves the same problem as the calculateHeuristicValue function, but we
# decided to keep it because it uses a different but interesting approach
def matrixRating(matrix):
    rating = 0
    x = 0
    y = 0
    coordinatesSolved = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]
    for i in range(3):
        for j in range(3):
            value = matrix[j][i]
            # print(value)
            x = coordinatesSolved[value-1][0] + j
            y = coordinatesSolved[value-1][1] + i
            rating = rating + x + y
    
    return rating

# greedy algorithm uses the same logic as the breadth first algorithm but
# in addition it uses a heuristic to find the solution
def greedy(matrix):
    found = False
    visited = [] # list
    queue = deque()
    queue.append(matrix)
    counter = 0
    # while the queue is not empty and the solution has not been found
    while queue and not found:
        node = queue.popleft()
        counter = counter + 1
        if node not in visited:
            if isSolved(node):
                # TODO: do not print following lines in the final version for
                # time performance
                # print("Actual node: " + str(node))
                # print("puzzle solved")
                # print("After " + str(counter) + " iterations")
                queue.clear() # empty the queue
                found = True

            addToVisited(node, visited)

            # all 4 possible moves will be checked and only the one with the lowest heuristic value will be added to the queue
            if not found:
                up,right,down,left = allMoves(node)
                xAxis, yAxis = findZero(node)
                
                # we use a vector of 4 elements to store the heuristic values of the 4 possible moves
                # the heuristic value of a move is -1 if the move is not possible
                heuristicValues = [-1, -1, -1, -1]

                if up:
                    newNode = goUp(node, xAxis, yAxis)
                    if newNode not in visited:
                        heuristicValues[0] = calculateHeuristicValue(newNode)
                    newNode = None

                if right:
                    newNode = goRight(node, xAxis, yAxis)
                    if newNode not in visited:
                        heuristicValues[1] = calculateHeuristicValue(newNode)
                    newNode = None

                if down:
                    newNode = goDown(node, xAxis, yAxis)
                    if newNode not in visited:
                        heuristicValues[2] = calculateHeuristicValue(newNode)
                    newNode = None

                if left:
                    newNode = goLeft(node, xAxis, yAxis)
                    if newNode not in visited:
                        heuristicValues[3] = calculateHeuristicValue(newNode)
                    newNode = None

                # find the move with the lowest heuristic value
                minHeuristic = 0

                # find the first move that is possible
                for i in range(4):
                    if heuristicValues[i] != -1:
                        minHeuristic = i
                        break

                # find the move with the lowest heuristic value
                for i in range(4):
                    if heuristicValues[i] != -1:
                        if heuristicValues[i] < heuristicValues[minHeuristic]:
                            minHeuristic = i
                
                # add the move with the lowest heuristic value to the queue
                # there is no need to check if the move is possible because it has already been checked
                if minHeuristic == 0:
                    newNode = goUp(node, xAxis, yAxis)
                    queue.append(newNode)
                if minHeuristic == 1:
                    newNode = goRight(node, xAxis, yAxis)
                    queue.append(newNode)
                if minHeuristic == 2:
                    newNode = goDown(node, xAxis, yAxis)
                    queue.append(newNode)
                if minHeuristic == 3:
                    newNode = goLeft(node, xAxis, yAxis)
                    queue.append(newNode)

# generateSons function generates all the possible sons of a given matrix
def generateSons(matrix):
    matrixToVisit = []

    up,right,down,left = allMoves(matrix)
    xAxis, yAxis = findZero(matrix)

    if up:
        newMatrix = goUp(matrix, xAxis, yAxis)
        matrixToVisit.append(newMatrix)

    if right:
        newMatrix = goRight(matrix, xAxis, yAxis)
        matrixToVisit.append(newMatrix)

    if down:
        newMatrix = goDown(matrix, xAxis, yAxis)
        matrixToVisit.append(newMatrix)
    if left:
        newMatrix = goLeft(matrix, xAxis, yAxis)
        matrixToVisit.append(newMatrix)

    return matrixToVisit

# IDS function uses the iterative deepening search algorithm to solve the
# 8 puzzle
def IDS(matrix):
    depthGoal = 0
    found = False
    while not found:
        # print("Nivel " + str(depthGoal))
        # at the start of each iteration the visited list is cleared
        visited.clear()
        resultGivenLevel = IDSRecursive(matrix, depthGoal)
        if resultGivenLevel is not None:
            # print("puzzle solved")
            found = True
        depthGoal = depthGoal + 1

# IDSRecursive function is a recursive function that is used in the IDS algorithm
def IDSRecursive(matrix, level):
    if isSolved(matrix):
        return matrix
    if level == 0:
        # base case of the recursion, just return None because answer not found
        return None
    else:
        sons = generateSons(matrix)
        # for each son of the matrix, check if it has already been visited
        # if not, add it to the visited list and call the recursive function
        for son in sons:
            if son not in visited:
                visited.append(son)
                answer = IDSRecursive(son, level-1)
                # only case in which the answer is not None is when the puzzle
                # has been solved
                if answer is not None:
                    return answer
    return None

# idsStar function uses the IDS algorithm in addition to the use of a
# heuristic to solve the 8 puzzle
def idsStar(matrix):
    threshold = calculateHeuristicValue(matrix)
    found = False

    while not found:
        movementCost = 0
        resultGivenLevel, newThreshold = idsStarRecursive(matrix, threshold, movementCost)
        if resultGivenLevel is not None:
            # print("puzzle solved")
            # print("Solution is: " + str(resultGivenLevel))
            found = True
        threshold = newThreshold # update the threshold with the new threshold

# recursive function for the a_star algorithm
def idsStarRecursive(matrix, threshold, movementCost):
    estimatedCost = calculateHeuristicValue(matrix) + movementCost # hope that works
    if estimatedCost > threshold:
        return None, estimatedCost
    if isSolved(matrix):
        return matrix, threshold

    sons = generateSons(matrix)
    minimumCost = 1000000000 # a very big number
    for son in sons:
        resultGivenLevel, newThreshold = idsStarRecursive(son, threshold, movementCost+1)
        # only case in which the resultGivenLevel is not None is when the
        # puzzle has been solved
        if resultGivenLevel is not None:
            return resultGivenLevel, threshold
        if newThreshold < minimumCost:
            minimumCost = newThreshold

    # the calculated threshold is the minimum cost of the sons
    return None, minimumCost

# isTableSolvable function checks if a matrix is solvable
# the function uses the inversion count, if the inversion count is even then
# the matrix is solvable
def isTableSolvable(matrix):
    # Flatten the matrix and include 0 if it's present
    flatMatrix = [elem for row in matrix for elem in row]
    if 0 not in flatMatrix:
        flatMatrix.append(0)

    # Count inversions
    inversions = 0
    for i in range(len(flatMatrix)):
        for j in range(i + 1, len(flatMatrix)):
            if flatMatrix[i] > flatMatrix[j] and flatMatrix[j] != 0:
                inversions += 1

    # Check if the puzzle is solvable based on inversion count and blank position
    blankRowFromBottom = (len(matrix) - 1) - (flatMatrix.index(0) // len(matrix[0]))
    if len(matrix[0]) % 2 == 0:
        return (inversions % 2 == 0) == (blankRowFromBottom % 2 == 1)
    else:
        return inversions % 2 == 0