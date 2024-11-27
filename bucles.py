"""
Los bucles permiten repetir un conjunto de instrucciones varias veces, hasta que 
se cumpla una condición. En Python, existen dos tipos de bucles:

while: 
Machine Learning Y Deep Learning 
Se ejecuta mientras se cumpla una condición. 
while condicion: 
instruccion 
for: 
Permite iterar sobre una secuencia de elementos. 
for elemento in secuencia: 
instruccion
"""

#Imprimir números del 1 al 5: 
for numero in range(1, 6): 
    print(numero) 
#Buscar un elemento específico en una lista: 
lista = [1, 2, 3, 4, 5] 
i = 0 
encontrado = False 
while i < len(lista) and not encontrado: 
    if lista[i] == 3: 
        print("Número encontrado en la posición:", i) 
        encontrado = True 
    i += 1 