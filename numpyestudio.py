import numpy as np

"""
Crear matrices y arreglos: NumPy proporciona funciones para crear matrices 
y arreglos multidimensionales de manera rápida y sencilla. Por ejemplo, 
puedes crear una matriz NumPy a partir de una lista o tupla: 
"""
arr = np.array([1,2,3,4,5])
print(arr)

"""
También puedes crear matrices específicas, como matrices de ceros, unos 
o matrices identidad: 

"""
zeros_matrix = np.zeros((3,3))
print(zeros_matrix)

ones_matrix = np.ones((2,4))
print(ones_matrix)

identity_matrix = np.eye(3) #Matriz identidad de tamaño 3x3
print(identity_matrix)

"""
Operaciones matemáticas: NumPy permite realizar una amplia variedad de 
operaciones matemáticas en matrices y arreglos. Puedes realizar 
operaciones aritméticas básicas, como suma, resta, multiplicación y división, 
así como funciones matemáticas más avanzadas: 
"""

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

#SUMA
result_sum = a + b
print(result_sum)

#PRODUCTO PUNTO
dot_product = np.dot(a,b)
print(dot_product)

#FUNCIONES MATEMATICAS
sin_values = np.sin(a)
print(sin_values)

"""
Indexación y rebanado: Puedes acceder a elementos individuales de una 
matriz NumPy utilizando la indexación y el rebanado:
"""

arr = np.array([[1,2,3],[4,5,6]])

# Acceder a un elemento

element = arr[0,1] # Accede al elemento en la primera fila, segunda columna 
print(element)

#Rebanar una matriz 

slice_arr = arr[:,1:] # Rebanar todas las filas, desde la segunda columna en adelante
print(slice_arr)

"""
Funciones de agregación y estadísticas: NumPy proporciona funciones para 
calcular estadísticas sobre matrices y arreglos, como la media, la mediana, 
la desviación estándar, etc.: 
"""
arr = np.array([[1,2,3],[4,5,6]])
print()

#Calcular la media 
mean_value = np.mean(arr)

#Calcular la mediana
median_value = np.median(arr)

#Calcular la desviación estándar 
std_deviation = np.std(arr)