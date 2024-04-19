import os
import eightPuzzleSolver
import time
import psutil
import matrices
          
class App():
    def __init__(self):
        print('App is initialized')

    def run(self):
        print('App is running')

        # previous format was better because it shows the matrix in a more readable way
        # but it stops being viable when the user has to choose a matrix among 20
        # matrixId = int(input("Choose matrix to solve from 0 to 19: "))
        # selected_matrix = matrices.matricesMaping.get(matrixId)

        # selected_matrix = matrices.generar_matriz_aleatoria()
        print("solving the puzzle: ")
        dicMatrices = matrices.leer_matrices_desde_txt('matrices.txt')
        
        matrizId = int(input("Choose a matrix between 0 and 19: "))
        selected_matrix = matrices.seleccionar_matriz(dicMatrices,matrizId)
        print(selected_matrix)
        if eightPuzzleSolver.isTableSolvable(selected_matrix) == False:
            print("\nThe puzzle is not solvable")
        else:
            print("\nThe puzzle is solvable")
        algorithmId = int(input("\nChoose algorithm to solve the puzzle: \n0. Ancho primero\n1. Greedy\n2. IDS\n3. IDS star\n"))

            # Breadth First
        if algorithmId == 0:
            print("Executing breadthFirst")
            startTime = time.time()
            eightPuzzleSolver.breadthFirst(selected_matrix)
            endTime = time.time()
            print("Time elapsed in seconds: ", endTime - startTime)
        
        # Greedy
        elif algorithmId == 1:
            print("Executing greedy")
            startTime = time.time()
            eightPuzzleSolver.greedy(selected_matrix)
            endTime = time.time()
            print("Time elapsed in seconds: ", endTime - startTime)
        
        # IDS
        elif algorithmId == 2:
            print("Executing IDS")
            startTime = time.time()
            eightPuzzleSolver.IDS(selected_matrix)
            endTime = time.time()
            print("Time elapsed in seconds: ", endTime - startTime)
        
        # IDS star
        elif algorithmId == 3:
            print("Executing IDS star")
            startTime = time.time()
            eightPuzzleSolver.idsStar(selected_matrix)
            endTime = time.time()
            print("Time elapsed in seconds: ", endTime - startTime)
        
        # Invalid algorithm id
        else:
            print("Invalid algorithm id")
            return

        # Get memory usage
        process = psutil.Process()
        memoryUsage = process.memory_info().rss  # in bytes
        print("Memory Usage:", memoryUsage, "bytes")
