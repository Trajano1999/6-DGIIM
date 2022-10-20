# IMPORTS

import random

# FUNCIONES

# muestra la cadena sin elementos de vector
def mostrarCadena(mi_cadena):
    for elem in mi_cadena:
        print(elem, end="")

# comprueba si la cadena recibida es correcta
def cadenaCorrecta(la_cadena):
    suma = 0
    for elem in la_cadena:
        if suma < 0:
            return False

        if elem == '[':
            suma+=1
        else:
            suma-=1

    if suma == 0:
        return True
    else:
        return False

# MAIN

cadena = []
num_corchetes = random.randint(1, 20)

for it in range(0, num_corchetes):
    aleatorio = random.randint(0,1)
    if aleatorio == 0:
        cadena.extend('[')  
    else:
        cadena.extend(']')

print("Cadena : ", end=""); mostrarCadena(cadena)

if num_corchetes%2 == 0 and cadenaCorrecta(cadena):
    print("\nLa cadena es satisfactoria :)")
else:
    print("\nLa cadena tiene algún error :(")
