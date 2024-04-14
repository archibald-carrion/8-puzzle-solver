import os
import IA   # TODO: change name of the file to something more significant
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

        # print("Choose matrix to solve from 0 to 19:\n")
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
        
        if IA.isTableSolvable(selected_matrix) == False:
            print("The puzzle is not solvable")
        else:
            print("The puzzle is solvable")

            # Breadth First
            if algorithm_id == 0:
                print("Executing breadthFirst")
                start_time = time.time()
                IA.breadthFirst(selected_matrix)
                end_time = time.time()
                print("Time elapsed in seconds: ", end_time - start_time)
            
            # Greedy
            elif algorithm_id == 1:
                print("Executing greedy")
                start_time = time.time()
                IA.greedy(selected_matrix)
                end_time = time.time()
                print("Time elapsed in seconds: ", end_time - start_time)
            
            # IDS
            elif algorithm_id == 2:
                print("Executing IDS")
                start_time = time.time()
                IA.IDS(selected_matrix)
                end_time = time.time()
                print("Time elapsed in seconds: ", end_time - start_time)
            
            # IDS star
            elif algorithm_id == 3:
                print("Executing IDS star")
                start_time = time.time()
                IA.IDS_star(selected_matrix)
                end_time = time.time()
                print("Time elapsed in seconds: ", end_time - start_time)
            
            # Invalid algorithm id
            else:
                print("Invalid algorithm id")
                return


            #Ancho Prime


            
            # tiempo_transcurrido = fin_tiempo - inicio_tiempo

            # print(f"Tiempo transcurrido en algoritmo ancho primero: {tiempo_transcurrido} segundos")

            #Greedy
            # inicio_tiempo = time.time()
            # IA.greedy(selected_matrix)

            # fin_tiempo = time.time()
            
            # tiempo_transcurrido = fin_tiempo - inicio_tiempo

            # print(f"Tiempo transcurrido en algoritmo greedy: {tiempo_transcurrido} segundos")
            
            # #IDS
            # inicio_tiempo = time.time()

            # IA.IDS(selected_matrix)

            # fin_tiempo = time.time()
            
            # tiempo_transcurrido = fin_tiempo - inicio_tiempo

            # print(f"Tiempo transcurrido en algoritmo IDS: {tiempo_transcurrido} segundos")
            
            # #IDS star

            # inicio_tiempo = time.time()
            # IA.IDS_star(selected_matrix)

            # fin_tiempo = time.time()
            
            # tiempo_transcurrido = fin_tiempo - inicio_tiempo

            # print(f"Tiempo transcurrido en algoritmo IDA: {tiempo_transcurrido} segundos")


        
        

        


        