import os
import IA   # TODO: change name of the file to something more significant


matrix_solvable = [[1, 4, 3],
                   [7, 6, 5],
                   [8, 2, 0]]

class App():
    def __init__(self):
        print('App is initialized')

    def run(self):
        print('App is running')
        print("solving the puzzle: ")
        print(matrix_solvable)
        IA.breadthFirst(matrix_solvable)
        #print(matrix_solvable)