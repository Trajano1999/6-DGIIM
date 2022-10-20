# IMPORTS  

import math

# FUNCIONES

# función booleana que indica si un número es o no primo
def esPrimo(num):
    continuar = True
    for menor in range(2, int(math.sqrt(num)+1)):
        if num % menor == 0 and continuar:
            continuar = False
    return continuar

# MAIN

# lectura del valor a estudiar
print("Introduce un número natural :", end=" ")
valor = int(input())

# bucle de búsqueda
if valor > 2:
    print(2)

for num in range(1, valor, 2):
    if num != 1 and esPrimo(num):
        print(num)
