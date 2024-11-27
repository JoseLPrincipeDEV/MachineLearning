""""
Las condicionales en Python posibilitan ejecutar una o varias instrucciones si se 
cumple una condición. La estructura básica de un condicional en Python es la 
siguiente: 

if condicion: 
    instruccion 
"""

if True:
    print(True)

"""
La condición es una expresión lógica que debe evaluar a verdadero o falso. Si la 
condición se cumple, se ejecuta la instrucción. 
 
Además del `if`, existen otras estructuras condicionales en Python: 
 
if - else: 
Permite ejecutar una instrucción si se cumple la condición y otra si no se cumple. 

"""
falso = False

if falso == True: 
    print(falso)
else:
    print(falso)

"""
if - elif - else: 
Permite evaluar múltiples condiciones, ejecutando una instrucción diferente para 
cada una. 
 
if condicion1: 
    instruccion1 
elif condicion2: 
    instruccion2 
... 
else: 
    instruccionN
"""

valor = 2

if valor == 1:
    print(True)
elif valor == 2:
    print(True)
else:
    print(False)