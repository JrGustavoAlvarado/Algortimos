#1. Buscar el numero menor en mi array 
#2. Crear dos subarrays para llevar el control de mi algortimo 
#3. Imprimir el resultado del ordenamiento 
import sys 
array =[5, 80, 9, 20, 32, 14,32,72,7]

def selectionSort(array):
    #recorrer todo nuestro array
    for i in range(len(array)):
        
        #Encontrar el valor minimo restante dentro de nuestro array desordenado 
         idxDes = i
         for j in range(i+1, len(array)):
             if array[idxDes] > array[j]:
                 idxDes = j 
                
         #ya que encontramos el minomo lo vamos a cambiar por el primer valor de nuestro array desordenado 
         array[i], array[idxDes] = array[idxDes], array[i]       
         
#Ejecutar la función 

selectionSort(array)
print("Array Ordenado:")
for i in range(len(array)):
    print("%d" %array[i]) 
             