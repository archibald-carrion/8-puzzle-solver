# # Dictionary containing the matrix variables from py

# matrixSolvable0 = [[0, 8, 2],
#                      [1, 4, 3],
#                      [6, 5, 7]]

# matrixSolvable1 = [[1, 2, 3],
#                      [4, 8, 7],
#                      [6, 0, 5]]
                     
# matrixSolvable2 = [[1, 2, 3],
#                      [4, 6, 8],
#                      [7, 5, 0]]

# matrixSolvable3 = [[7, 3, 6],
#                      [5, 1, 2],
#                      [8, 0, 4]]

# matrixSolvable4 = [[1, 2, 5],
#                      [4, 0, 8],
#                      [6, 7, 3]]

# matrixSolvable5 = [[0, 1, 3],
#                      [8, 2, 7],
#                      [4, 6, 5]]
                     
# matrixSolvable6 = [[1, 3, 8],
#                      [7, 2, 4],
#                      [5, 6, 0]]

# matrixSolvable7 = [[4, 8, 1],
#                      [2, 0, 7],
#                      [6, 3, 5]]

# matrixSolvable8 = [[2, 8, 5],
#                      [6, 7, 0],
#                      [1, 3, 4]]

# matrixSolvable9 = [[0, 7, 6],
#                      [8, 4, 3],
#                      [2, 1, 5]]
                     
# matrixSolvable10 = [[4, 0, 7],
#                      [2, 5, 3],
#                      [6, 8, 1]]

# matrixSolvable11 = [[1, 5, 0],
#                      [3, 8, 2],
#                      [4, 6, 7]]
                     
# matrixSolvable12 = [[4, 3, 8],
#                      [1, 6, 0],
#                      [7, 2, 5]]

# matrixSolvable13 = [[2, 3, 6],
#                      [1, 7, 0],
#                      [8, 5, 4]]

# matrixSolvable14 = [[0, 2, 3],
#                      [7, 4, 5],
#                      [1, 6, 8]]

# matrixSolvable15 = [[1, 2, 5],
#                      [6, 0, 8],
#                      [3, 7, 4]]
                     
# matrixSolvable16 = [[0, 6, 4],
#                      [7, 8, 1],
#                      [3, 5, 2]]

# matrixSolvable17 = [[3, 0, 7],
#                      [4, 2, 5],
#                      [1, 8, 6]]

# matrixSolvable18 = [[7, 6, 1],
#                      [5, 0, 2],
#                      [3, 4, 8]]

# matrixSolvable19 = [[4, 2, 7],
#                      [8, 3, 1],
#                      [6, 5, 0]]

# # unsolvable matrix
# matrixUnsolvable1 = [[1, 7, 3],
#                        [0, 6, 2],
#                        [8, 4, 5]]

# matrixUnsolvable2 = [[1, 2, 3],
#                        [4, 5, 6],
#                        [8, 7, 0]]

import random

def generar_matriz_aleatoria():
    numeros_disponibles = list(range(9))
    matriz = [[None, None, None], [None, None, None], [None, None, None]]
    
    for i in range(3):
        for j in range(3):
            numero = random.choice(numeros_disponibles)
            matriz[i][j] = numero
            numeros_disponibles.remove(numero) 
    
    return matriz

def guardar_matrices_en_txt(nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for _ in range(20):
            matriz = generar_matriz_aleatoria()
            archivo.write(','.join(map(str, matriz[0])) + '\n')
            archivo.write(','.join(map(str, matriz[1])) + '\n')
            archivo.write(','.join(map(str, matriz[2])) + '\n')
            archivo.write('\n')

def leer_matrices_desde_txt(nombre_archivo):
    matrices_dict = {}
    with open(nombre_archivo, 'r') as archivo:
        matrices = archivo.read().split('\n\n')
        for idx, matriz_str in enumerate(matrices, 0):
            if matriz_str.strip():
                matriz = [[int(num) for num in fila.split(',')] for fila in matriz_str.split('\n')]
                matrices_dict[idx] = matriz
    return matrices_dict

def imprimir_diccionario_matrices(diccionario):
    for clave, matriz in diccionario.items():
        print(f'Matriz {clave}:')
        for fila in zip(*matriz):
            print('\t'.join(map(str, fila)))
        print()

def seleccionar_matriz(diccionario, indice):
    if indice in diccionario:
        matriz_seleccionada = diccionario[indice]
        return matriz_seleccionada
    else:
        print(f'No se encontró una matriz con el índice {indice} en el diccionario.')
