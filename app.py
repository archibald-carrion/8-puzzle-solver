import os
import IA   # TODO: change name of the file to something more significant
import time
import matrices
  
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


        # previous format was better because it shows the matrix in a more readable way
        # but it stops being viable when the user has to choose a matrix among 20
        # print("Choose matrix to solve from 0 to 19:\n")
        matrix_id = int(input("Choose matrix to solve from 0 to 19: "))
        selected_matrix = matrices.matrices_maping.get(matrix_id)

        # selected_matrix

        # add input to now wich algorithm to use

        # print("1.matrix_solvable_1")
        # print(str(matrix.matrix_solvable_1))

        # print("2.matrix_solvable_2")
        # print(str(matrix_solvable_2))

        # print("3.matrix_solvable_3")
        # print(str(matrix_solvable_3))

        # print("4.matrix_unsolvable_1")
        # print(str(matrix_unsolvable_1))

        # print("5.matrix_unsolvable_2")
        # print(str(matrix_unsolvable_2))

        # print("Escoja una matriz: ")


        # if id == 1:
        #     matrix_solvable = matrix_solvable_1

        # if id == 2:
        #     matrix_solvable = matrix_solvable_2

        # if id == 3:
        #     matrix_solvable = matrix_solvable_3

        # if id == 4:
        #     matrix_solvable = matrix_unsolvable_1

        # if id == 5:
        #     matrix_solvable = matrix_unsolvable_2

        print("solving the puzzle: ")
        print(selected_matrix)
        
        if isTableSolvable(selected_matrix) == False:
            print("The puzzle is not solvable")
        else:
            print("The puzzle is solvable")
            #Ancho Prime
            inicio_tiempo = time.time()

            IA.breadthFirst(selected_matrix)

            fin_tiempo = time.time()
            
            tiempo_transcurrido = fin_tiempo - inicio_tiempo

            print(f"Tiempo transcurrido en algoritmo ancho primero: {tiempo_transcurrido} segundos")

            #Greedy
            inicio_tiempo = time.time()
            IA.greedy(selected_matrix)

            fin_tiempo = time.time()
            
            tiempo_transcurrido = fin_tiempo - inicio_tiempo

            print(f"Tiempo transcurrido en algoritmo greedy: {tiempo_transcurrido} segundos")
            
            #IDS
            inicio_tiempo = time.time()

            IA.IDS(selected_matrix)

            fin_tiempo = time.time()
            
            tiempo_transcurrido = fin_tiempo - inicio_tiempo

            print(f"Tiempo transcurrido en algoritmo IDS: {tiempo_transcurrido} segundos")
            
            #IDS star

            inicio_tiempo = time.time()
            IA.IDS_star(selected_matrix)

            fin_tiempo = time.time()
            
            tiempo_transcurrido = fin_tiempo - inicio_tiempo

            print(f"Tiempo transcurrido en algoritmo IDA: {tiempo_transcurrido} segundos")


        
        

        


        