import os
import eight_puzzle_solver
import time
import matrices
          
class App():
    def __init__(self):
        print('App is initialized')

    def run(self):
        print('App is running')

        # previous format was better because it shows the matrix in a more readable way
        # but it stops being viable when the user has to choose a matrix among 20
        matrix_id = int(input("Choose matrix to solve from 0 to 19: "))
        selected_matrix = matrices.matrices_maping.get(matrix_id)

        algorithm_id = int(input("Choose algorithm to solve the puzzle: \n0. Ancho primero\n1. Greedy\n2. IDS\n3. IDS star\n"))

        print("solving the puzzle: ")
        print(selected_matrix)
        
        if eight_puzzle_solver.isTableSolvable(selected_matrix) == False:
            print("The puzzle is not solvable")
        else:
            print("The puzzle is solvable")

            # Breadth First
            if algorithm_id == 0:
                print("Executing breadthFirst")
                start_time = time.time()
                eight_puzzle_solver.breadthFirst(selected_matrix)
                end_time = time.time()
                print("Time elapsed in seconds: ", end_time - start_time)
            
            # Greedy
            elif algorithm_id == 1:
                print("Executing greedy")
                start_time = time.time()
                eight_puzzle_solver.greedy(selected_matrix)
                end_time = time.time()
                print("Time elapsed in seconds: ", end_time - start_time)
            
            # IDS
            elif algorithm_id == 2:
                print("Executing IDS")
                start_time = time.time()
                eight_puzzle_solver.IDS(selected_matrix)
                end_time = time.time()
                print("Time elapsed in seconds: ", end_time - start_time)
            
            # IDS star
            elif algorithm_id == 3:
                print("Executing IDS star")
                start_time = time.time()
                eight_puzzle_solver.IDS_star(selected_matrix)
                end_time = time.time()
                print("Time elapsed in seconds: ", end_time - start_time)
            
            # Invalid algorithm id
            else:
                print("Invalid algorithm id")
                return
