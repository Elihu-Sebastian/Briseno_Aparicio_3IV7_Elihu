print("ingrese el orden de la matriz a calcular")
filas1 = int( input())
columnas1 = int( input())

matrizA = []
for i in range(filas1):
    matrizA.append([0] * columnas1)
    
print("ingrese la matriz A")
for fila in range(filas1):
    for columna in range(columnas1):
        matrizA[fila][columna] = float(input(f'ingrese la posicion {fila}. {columna}: '))
        
print('\nMatriz inicial\n')
for i in matrizA:
    print(i)

matrizB = []
for i in range(filas1):
    matrizB.append([0] * columnas1)
    
        
for fila in range(filas1):
    for columna in range(columnas1):
        matrizB [fila][columna] = matrizA[columna][fila]
        
print('\nMatriz Transpuesta\n')
for i in matrizB:
    print(i)