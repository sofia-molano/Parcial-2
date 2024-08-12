A=[4,0,3,6.2,1,0]

#EJERCICIO 1
#Elementos repetidos en una lista

def repetidos(lista):
    for i in range(len(lista)):
        variable=lista.count(i)
        if variable>1:
            return True

print('Hay elementos repetidos en la lista:',repetidos(A))

#EJERCICIO 2
#Cadena con dos o más vocales, imprimirla y si no  que imprima 'No existe'

def vocales(lista):
    vocales=('a','e','i','o','u')
    for x in lista:
        contar=lista.count(vocales)
        if contar>=2:
            print('Si')
        else:
            print('No')


B=('Los estudiantes son')
#print(vocales(B))

#EJERCICIO 3
#Elementos de una lista que no tiene la segunda
 
def comparar(lista1,lista2):
    lista_f=[]
    for i in range(len(lista1)):
        x=lista2.find(lista1[i])
        if x==None:
            lista_f+=x
        
            return lista_f
        

    
C=('Los estudiantes son universitarios')
print(comparar(B,C))


#EJERCICIO 4
#Promedio de un arreglo

def promedio_arreglo(arreglo):
    promedio=0
    for x in arreglo:
        promedio+=x
    return promedio


print(promedio_arreglo(A))

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

    if m % 2 != 0: 
        mediana = A[m // 2]
    else:  
        mediana = (A[m // 2 - 1] + A[m // 2]) // 2
    
    return mediana

print (mediana_arreglo(A))