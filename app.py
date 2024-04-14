import os
import IA   # TODO: change name of the file to something more significant
import time

matrix_solvable_1 = [[1, 2, 3],
                     [4, 8, 7],
                     [6, 0, 5]]
                     
matrix_solvable_2 = [[1, 2, 3],
                     [4, 6, 8],
                     [7, 5, 0]]

matrix_solvable_3 = [[7, 3, 6],
                     [5, 1, 2],
                     [8, 0, 4]]

matrix_unsolvable_1 = [[1, 7, 3],
                       [0, 6, 2],
                       [8, 4, 5]]

matrix_unsolvable_2 = [[1, 2, 3],
                       [4, 5, 6],
                       [8, 7, 0]]


# # Function to check if the matrix is solvable
# # a matrix is solvable if the number of inversions is even
# # an inversion is when a number is greater than another number that is after it
# # 0 is not counted as a number in this case, only the numbers from 1 to 8
# # TODO: check if this is correct
# def isTableSolvable(matrix):
#     #Count the number of inversions
#     inversions = 0
#     #Create a list with the matrix
#     list_matrix = []
#     for i in range(3):
#         for j in range(3):
#             list_matrix.append(matrix[i][j])
#     #Count the number of inversions
#     for i in range(9):
#         for j in range(i+1,9):
#             if list_matrix[i] > list_matrix[j] and list_matrix[i] != 0 and list_matrix[j] != 0:
#                 inversions = inversions + 1
#     #If the number of inversions is odd, the matrix is not solvable
#     if inversions % 2 != 0:
#         return False
#     return True
  
def isTableSolvable(matrix):
    # Flatten the matrix and include 0 if it's present
    flat_matrix = [elem for row in matrix for elem in row]
    if 0 not in flat_matrix:
        flat_matrix.append(0)

    # Count inversions
    inversions = 0
    for i in range(len(flat_matrix)):
        for j in range(i + 1, len(flat_matrix)):
            if flat_matrix[i] > flat_matrix[j] and flat_matrix[j] != 0:
                inversions += 1

    # Check if the puzzle is solvable based on inversion count and blank position
    blank_row_from_bottom = (len(matrix) - 1) - (flat_matrix.index(0) // len(matrix[0]))
    if len(matrix[0]) % 2 == 0:
        return (inversions % 2 == 0) == (blank_row_from_bottom % 2 == 1)
    else:
        return inversions % 2 == 0
          
class App():
    def __init__(self):
        print('App is initialized')

    def run(self):
        print('App is running')


        print("Which matrix, do you want to run:\n")
        print("1.matrix_solvable_1")
        print(str(matrix_solvable_1))

        print("2.matrix_solvable_2")
        print(str(matrix_solvable_2))

        print("3.matrix_solvable_3")
        print(str(matrix_solvable_3))

        print("4.matrix_unsolvable_1")
        print(str(matrix_unsolvable_1))

        print("5.matrix_unsolvable_2")
        print(str(matrix_unsolvable_2))

        print("Escoja una matrriz: ")

        id = int(input())

        if id == 1:
            matrix_solvable = matrix_solvable_1

        if id == 2:
            matrix_solvable = matrix_solvable_2

        if id == 3:
            matrix_solvable = matrix_solvable_3

        if id == 4:
            matrix_solvable = matrix_unsolvable_1

        if id == 5:
            matrix_solvable = matrix_unsolvable_2

        print("solving the puzzle: ")
        print(matrix_solvable)
        
        if isTableSolvable(matrix_solvable) == False:
            print("The puzzle is not solvable")
        else:
            print("The puzzle is solvable")
            #Ancho Prime
            inicio_tiempo = time.time()

            IA.breadthFirst(matrix_solvable)

            fin_tiempo = time.time()
            
            tiempo_transcurrido = fin_tiempo - inicio_tiempo

            print(f"Tiempo transcurrido en algoritmo ancho primero: {tiempo_transcurrido} segundos")

            #Greedy
            inicio_tiempo = time.time()
            IA.greedy(matrix_solvable)

            fin_tiempo = time.time()
            
            tiempo_transcurrido = fin_tiempo - inicio_tiempo

            print(f"Tiempo transcurrido en algoritmo greedy: {tiempo_transcurrido} segundos")
            
            #IDS
            inicio_tiempo = time.time()

            IA.IDS(matrix_solvable)

            fin_tiempo = time.time()
            
            tiempo_transcurrido = fin_tiempo - inicio_tiempo

            print(f"Tiempo transcurrido en algoritmo IDS: {tiempo_transcurrido} segundos")
            
            #IDS star

            inicio_tiempo = time.time()
            IA.IDS_star(matrix_solvable)

            fin_tiempo = time.time()
            
            tiempo_transcurrido = fin_tiempo - inicio_tiempo

            print(f"Tiempo transcurrido en algoritmo IDA: {tiempo_transcurrido} segundos")


        
        

        


        