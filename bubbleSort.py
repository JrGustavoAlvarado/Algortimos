#1. - Comenzar a realizar comparaciones de adyacentes 
#. Repetir hasta tener una pasada completa si ningun swap 


def bubbleSort (array):
    n = len(array)
    
    for i in range(n):
    
        for j in range(0, n-i-1):
            if array[j] > array [j+1] :
                array[j], array [j+1] = array[j+1], array[j]
                
array = [2010, 1200, 2, 3, 4, 5, 10, 800] 
bubbleSort(array)

print("El arreglo ordenado de forma ascendente:")
for i in range(len(array)):
    print("%d"%array[i]),               