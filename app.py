import os
import IA   # TODO: change name of the file to something more significant
import time



# matrix_solvable = [[1, 4, 3],
#                    [7, 6, 5],
#                    [8, 2, 0]]

# matrix_solvable = [[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 0, 8]]

# matrix_solvable = [[1, 2, 3],
#                    [4, 5, 6],
#                    [0, 7, 8]]

matrix_solvable_1 = [[1, 2, 3],
                     [4, 8, 7],
                     [6, 0, 5]]
                     
matrix_solvable_2 = [[1, 2, 3],
                     [4, 6, 8],
                     [7, 5, 0]]

matrix_solvable_3 = [[7, 3, 6],
                     [5, 1, 2],
                     [8, 0, 4]]

matrix_unsolvable_1 = [[1, 2, 3],
                       [6, 0, 7],
                       [8, 4, 5]]

matrix_unsolvable_2 = [[7, 6, 3],
                       [5, 1, 2],
                       [8, 0, 4]]



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


        
        

        


        