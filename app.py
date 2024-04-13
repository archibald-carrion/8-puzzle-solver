import os
import IA   # TODO: change name of the file to something more significant


matrix_solvable = [[1, 4, 3],
                    [7, 6, 5],
                    [8, 2, 0]]

#matrix_solvable = [[1, 2, 3],
#                   [4, 5, 6],
#                   [7, 0, 8]]
class App():
    def __init__(self):
        print('App is initialized')

    def run(self):
        print('App is running')
        print("solving the puzzle: ")
        print(matrix_solvable)
        # IA.breadthFirst(matrix_solvable)
        # IA.greedy(matrix_solvable)
        IA.IDS(matrix_solvable)