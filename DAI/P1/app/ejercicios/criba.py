# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

import math

# -----------------------------------------------------------------------------
# FUNCIONES
# -----------------------------------------------------------------------------

# función booleana que indica si un número es o no primo
def esPrimo(num):
    continuar = True
    for menor in range(2, int(math.sqrt(num)+1)):
        if num % menor == 0 and continuar:
            continuar = False
    return continuar

# funcion que devuelve un vector de todos los primos menores que el valor recibido
def cribaEratostenes(tamano):
    resultado = []
    if tamano > 2:
        resultado.append(2)

    for num in range(1, tamano, 2):
        if num != 1 and esPrimo(num):
            resultado.append(num)

    return resultado

# muestra los valores de un vector en columna
def mostrarValores(vector):
    for num in vector:
        print(num)

# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    print("Introduce un número natural :", end=" ")
    valor = int(input())

    primos = cribaEratostenes(valor)
    mostrarValores(primos)
