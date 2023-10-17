import random

#vector_1 aleatorio
def Vector_1():
    return [random.randint(1, 20) for _ in range(50)]

#vector_2 eliminar numeros repetidos 
def Vector_2_SinRepetir(vector):
    vector_2_sin_repetir = []
    for num in vector:
        if num not in vector_2_sin_repetir:
            vector_2_sin_repetir.append(num)
    return vector_2_sin_repetir

#vector_3 cantidad de repeticiones 
def v_1_Repeticiones(vector1, vector2):
    conteo = {}
    for num in vector2:
        conteo[num] = vector1.count(num)
    return conteo

# Lea un número por teclado e informe cuantas veces se repite en el primer vector
def contar_apariciones_en_vector1(vector1, numero_ingresado):
   count = 0
   for num in vector1:
        if num == numero_ingresado:
         count +=1
   return count

numero_ingresado=int(input("ingrese el numero que quiere buscar en el vector1"))

#Cuente cuantos elementos tiene cada uno de los vectores
def cantidad_elementos_vectores(vector1,vector2,vector3):
 return len(vector1)+ len(vector2)+ len(vector3)

#llamado a las funciones de los vectores 
primer_vector = Vector_1()
segundo_vector = Vector_2_SinRepetir(primer_vector)
tercer_vector = v_1_Repeticiones(primer_vector , segundo_vector)
apariciones_numero_ingresado = contar_apariciones_en_vector1(primer_vector , numero_ingresado)
elementos_vectores= cantidad_elementos_vectores (primer_vector,segundo_vector,tercer_vector)

#imprimir rsultados
print("los números almacenados aleatoriamente en el vector_1 son: ")
print(primer_vector)

print("segundo vector sin repetir valores:")
print(segundo_vector)

print("cantidad de repeticiones del vector_1:")
print(f"la cantidad de repeticiones del vector_1 son:{tercer_vector}")

print("la cantidad de apariciones del número buscado son:")
print(f"El número {numero_ingresado} se repite {apariciones_numero_ingresado} veces en vector 1.")

print("la cantidad de elementos de los vectores son=")
print(f"Vector 1 tiene {len(primer_vector)} elementos.")
print(f"Vector 2 tiene {len(segundo_vector)} elementos.")
print(f"Vector 3 tiene {len(tercer_vector)} elementos.")

#gracias por utilizar este programa
print("GRACIAS POR USAR ESTE PROGRAMA")



