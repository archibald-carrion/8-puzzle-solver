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


# def heuristic(matrix):
#     for number in matrix:
def findZero():
    x_axis, y_axis = 0, 0
    found = False
    while not(found) and y_axis < 3:
        x_axis = 0
        while not(found) and x_axis < 3:
            if matrix_solvable[y_axis][x_axis] == 0:
                found = True
            else:
                x_axis = x_axis + 1
        if not(found):
            y_axis = y_axis + 1
        
    
    return x_axis, y_axis

def tryMove():
    #find zero
    x_axis, y_axis = findZero()
    
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

print(matrix_solvable)
tryMove()
print(matrix_solvable)