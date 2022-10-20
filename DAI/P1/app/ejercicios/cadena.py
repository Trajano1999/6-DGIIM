# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

import random

# -----------------------------------------------------------------------------
# VARIABLES GLOBALES
# -----------------------------------------------------------------------------

mensaje_satisfactorio = "\nLa cadena es satisfactoria :)"
mensaje_error         = "\nLa cadena tiene algún error :("

# -----------------------------------------------------------------------------
# FUNCIONES
# -----------------------------------------------------------------------------

# genera una cadena de corchetes de tamaño num
def generarCadena(num):
    cadena = []
    for it in range(0, num):
        aleatorio = random.randint(0,1)
        if aleatorio == 0:
            cadena.extend('[')  
        else:
            cadena.extend(']')
    return cadena

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

# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    cadena = []
    num_corchetes = random.randint(1, 20)
    
    cadena = generarCadena(num_corchetes)
    print("Cadena : ", end=""); mostrarCadena(cadena)

    if num_corchetes%2 == 0 and cadenaCorrecta(cadena):
        print(mensaje_satisfactorio)
    else:
        print(mensaje_error)
