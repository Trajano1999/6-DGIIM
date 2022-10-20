# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

import re

# -----------------------------------------------------------------------------
# VARIABLES GLOBALES
# -----------------------------------------------------------------------------

mensaje_palabra = "La cadena es una palabra seguida de un espacio y una mayúscula :)"
mensaje_correo  = "La cadena es un correo electrónico :)"
mensaje_tarjeta = "La cadena es una tarjeta de crédito :)"
mensaje_error   = "Hay algún error en la cadena :("

# -----------------------------------------------------------------------------
# FUNCIONES
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

# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    print("Introduce la cadena a estudiar : ", end="")
    cadena = input()

    if identificarPalabra(cadena):
        print(mensaje_palabra)
    else:
        if identificarCorreo(cadena):
            print(mensaje_correo)
        else:
            if identificarTarjeta(cadena):
                print(mensaje_tarjeta)
            else:
                print(mensaje_error)
