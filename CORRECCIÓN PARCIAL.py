#CORRECCIÓN PARCIAL

#EJERCICIO 1
#Elementos repetidos en una lista

def repeticiones(lista):
    for i in lista:  
        variable = lista.count(i)
        if variable > 1: 
            return True 
    return False 

A = [4, 0, 3, 6, 2, 1]
print('Hay elementos repetidos en la lista:', repeticiones(A))

#EJERCICIO 2
#Cadena con dos o más vocales, imprimirla y si no hay que imprima 'No existe'

def vocales(lista):
    vocales = ('a', 'e', 'i', 'o', 'u')
    encontrada = False
    
    for x in lista:
        contar = 0
        for letra in x:
            if letra in vocales:
                contar += 1
        if contar >= 2:
            print(x)
            encontrada = True
    
    if not encontrada:
        print('No existe')

B = ['Los estudiantes son', 'prueba', 'zzzz', 'examen']
vocales(B)

#EJERCICIO 3
#Elementos de una lista que no tiene la segunda

def comparar(lista1, lista2):
    lista_f = []  
    
    for i in range(len(lista1)):
        if lista1[i] not in lista2:
            lista_f.append(lista1[i])
    
    return lista_f

B = ['Los', 'estudiantes', 'son', 'universitarios']
C = ['Los', 'universitarios']
print('Los elementos de la lista 1 que no estan en la 2 son:',comparar(B, C))


#EJERCICIO 4
#Promedio de un arreglo

def promedio_arreglo(arreglo):
    suma=0
    for x in arreglo:
        suma+=x
        promedio=(suma/(len(arreglo)))

    return promedio

print("El promedio del arreglo es:",promedio_arreglo(A))

#EJERCICIO 5
#Mediana de un arreglo 

def mediana_arreglo(A):
    m = len(A)

    for i in range(m):
        min_idx = i
        for j in range(i+1, m):
            if A[j] < A[min_idx]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]

    if m % 2 != 0:  # Si el número de elementos es impar
        mediana = A[m // 2]
    else:  # Si el número de elementos es par
        mediana = (A[m // 2 - 1] + A[m // 2]) // 2
    
    return mediana

print ("La mediana del arreglo es:",mediana_arreglo(A))
