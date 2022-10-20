# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

from flask import Flask, render_template

from ejercicios.fibonacci import Fibonacci
from ejercicios import criba
from ejercicios import cadena as ca
from ejercicios import eregulares as er
from generarSVG import randomSVG

app = Flask(__name__)

# -----------------------------------------------------------------------------
# ROUTES
# -----------------------------------------------------------------------------

# Página principal
@app.route('/')
def hello_world():
    return 'Hola Mundo :)'

# Ejercicio sucesión de Fibonacci
@app.route('/fibonacci/<int:valor>')
def routeFibonacci(valor):
    return str(Fibonacci(valor))

# Ejercicio criba de Eratóstenes
@app.route('/criba/<int:valor>')
def routeCriba(valor):
    return criba.cribaEratostenes(valor)

# Ejercicio cadena de corchetes
@app.route('/cadena/<string:cadena>')
def routeCadena(cadena):
    if ca.cadenaCorrecta(cadena):
        return 'La cadena es correcta'
    else:
        return 'La cadena es incorrecta'

# Ejercicio expresiones regulares
@app.route('/eregulares/<string:cadena>')
def routeEregulares(cadena):
    if er.identificarPalabra(cadena):
        return 'Es una palabra + espacio + mayúscula'
    else:
        if er.identificarCorreo(cadena):
            return 'Es un correo'
        else:
            if er.identificarTarjeta(cadena):
                return 'Es una tarjeta'
            else:
                return 'No es algo que pueda identificar'

# Ejercicio de mostrar una imagen
@app.route('/imagen')
def verImagen():
    return render_template("imagen.html")

# Ejercicio de error 404 : URL no definida
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Ejercicio de imágenes dinámicas
@app.route('/svg')
def routesvg():
    randomsvg = randomSVG()
    return '<h1>Random SVG<br/></h1>'+''.join(randomsvg)
