# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

import random
import math
import re

# -----------------------------------------------------------------------------
# FUNCIONES CRIBA ERATÓSTENES
# -----------------------------------------------------------------------------

# muestra los valores de un vector en columna
def mostrarValores(vector):
    for num in vector:
        print(num)

# función booleana que indica si un número es o no primo
def esPrimo(num):
    continuar = True
    for menor in range(2, int(math.sqrt(num)+1)):
        if num % menor == 0 and continuar:
            continuar = False
    return continuar

# devuelve un vector con todos los primos menores que el valor recibido
def cribaEratostenes(tamano):
    resultado = []
    if tamano > 2:
        resultado.append(2)

    for num in range(1, tamano, 2):
        if num != 1 and esPrimo(num):
            resultado.append(num)

    return resultado

# -----------------------------------------------------------------------------
# FUNCIÓN FIBONACCI
# -----------------------------------------------------------------------------

# función que encuentra el elemento num-ésimo de Fibonacci
def Fibonacci(num):
    first = 1; second = 1; suma = 0
    cont = 2
    while cont < num:
        cont+=1
        suma = first + second
        first = second
        second = suma
    return second

# -----------------------------------------------------------------------------
# FUNCIONES CADENA
# -----------------------------------------------------------------------------

# muestra la cadena sin elementos de vector
def mostrarCadena(mi_cadena):
    for elem in mi_cadena:
        print(elem, end="")

# genera una cadena de corchetes aleatoria de tamaño num
def generarCadena(num):
    cadena = []
    for it in range(0, num):
        aleatorio = random.randint(0,1)
        if aleatorio == 0:
            cadena.extend('[')  
        else:
            cadena.extend(']')
    return cadena

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
# FUNCIONES EXPRESIONES REGULARES
# -----------------------------------------------------------------------------

# indica si existe el patron en la cadena correspondiente
def comprobarCadena(patron, cadena):
    if patron.findall(cadena) == []:
        return False
    else:
        return True

# identifica una palabra seguida de un espacio y una letra mayúscula
def identificarPalabra(cadena):
    patron = re.compile('[a-zA-Z]*\s[A-Z]')
    return comprobarCadena(patron, cadena)

# identifica un correo electrónico válido
def identificarCorreo(cadena):
    patron = re.compile('[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}')
    return comprobarCadena(patron, cadena)

# identifica una tarjeta de crédito (separada por guiones o por espacios)
def identificarTarjeta(cadena):
    patron = re.compile('([0-9]{4}\s[0-9]{4}\s[0-9]{4}\s[0-9]{4}|[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4})')
    return comprobarCadena(patron, cadena)