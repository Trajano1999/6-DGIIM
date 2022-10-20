# VARIABLES

# ficheros de lectura y escritura
fichero_lectura = "./SFLectura.txt"
fichero_salida  = "./SFResultado.txt"

# FUNCIONES

# función que encuentra el elemento n-ésimo de Fibonacci
def Fibonacci(num):
    first = 1; second = 1; suma = 0
    cont = 2
    while cont < num:
        cont+=1
        suma = first + second
        first = second
        second = suma
    return second

# MAIN

# lectura de la primera palabra del fichero
fichero = open(fichero_lectura)
contenido = fichero.readline().split()[0]
fichero.close()

# escribimos el valor en la siguiente linea
fichero = open(fichero_salida, "w")
fichero.write(str(Fibonacci(int(contenido))))
fichero.close()
