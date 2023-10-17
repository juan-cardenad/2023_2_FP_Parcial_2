import random


def generar_matriz(filas, columnas, rango_inicio, rango_fin):
    matriz = []
    for _ in range(filas):
        fila = [random.randint(rango_inicio, rango_fin) for _ in range(columnas)]
        matriz.append(fila)
    return matriz

def sumar_fila(matriz, fila):
    return sum(matriz[fila])


def sumar_columna(matriz, columna):
    return sum(fila[columna] for fila in matriz)


def restar_matrices(matriz1, matriz2):
    matriz_diferencia = []
    for i in range(len(matriz1)):
        fila_dif = []
        for j in range(len(matriz1[i])):
            fila_dif.append(matriz2[i][j] - matriz1[i][j])
        matriz_diferencia.append(fila_dif)
    return matriz_diferencia


def multiplicar_matriz_numero(matriz, numero):
    matriz_producto_numero = []
    for i in range(len(matriz)):
        fila_prod = []
        for j in range(len(matriz[i])):
            fila_prod.append(matriz[i][j] * numero)
        matriz_producto_numero.append(fila_prod)
    return matriz_producto_numero


def multiplicar_matrices(matriz1, matriz2):
    matriz_producto = []
    for i in range(len(matriz1)):
        fila_prod = []
        for j in range(len(matriz2[0])):
            producto = 0
            for k in range(len(matriz2)):
                producto += matriz1[i][k] * matriz2[k][j]
            fila_prod.append(producto)
        matriz_producto.append(fila_prod)
    return matriz_producto


def sumar_diagonal(matriz):
    return sum(matriz[i][i] for i in range(len(matriz)))


def sumar_diagonal_inversa(matriz):
    return sum(matriz[i][len(matriz)-1-i] for i in range(len(matriz)))


def calcular_promedio(matriz):
    suma_total = sum(sum(fila) for fila in matriz)
    return suma_total / (len(matriz) * len(matriz[0]))



matriz_uno = generar_matriz(5, 5, 100, 200)


matriz_dos = generar_matriz(5, 5, 100, 200)
for i in range(5):
    for j in range(5):
        matriz_dos[i][j] = matriz_uno[i][j] ** (i + 2)


vector_suma_filas_uno = [sumar_fila(matriz_uno, fila) for fila in range(len(matriz_uno))]


vector_suma_columnas_dos = [sumar_columna(matriz_dos, columna) for columna in range(len(matriz_dos[0]))]


matriz_diferencia = restar_matrices(matriz_uno, matriz_dos)


numero = 5


matriz_producto_numero = multiplicar_matriz_numero(matriz_uno, numero)

matriz_tres = generar_matriz(5, 5, 100, 200)

matriz_producto = multiplicar_matrices(matriz_uno, matriz_tres)

suma_diagonal_uno = sumar_diagonal(matriz_uno)

suma_diagonal_inversa_dos = sumar_diagonal_inversa(matriz_dos)

media_matriz_producto = calcular_promedio(matriz_producto)

print("Matriz Uno:")
for fila in matriz_uno:
    print(fila)

print("Matriz Dos:")
for fila in matriz_dos:
    print(fila)

print("Vector de Suma de Filas de Matriz Uno:")
print(vector_suma_filas_uno)

print("Vector de Suma de Columnas de Matriz Dos:")
print(vector_suma_columnas_dos)

print("Matriz Diferencia (Matriz Dos - Matriz Uno):")
for fila in matriz_diferencia:
    print(fila)

print("Matriz Uno multiplicada por", numero, ":")
for fila in matriz_producto_numero:
    print(fila)

print("Producto de Matriz Uno y Matriz Tres:")
for fila in matriz_producto:
    print(fila)

print("Suma de la Diagonal Principal de Matriz Uno:", suma_diagonal_uno)
print("Suma de la Diagonal Inversa de Matriz Dos:", suma_diagonal_inversa_dos)
print("Media de la Matriz Producto:", media_matriz_producto)

                                