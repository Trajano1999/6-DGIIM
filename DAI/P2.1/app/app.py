# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

from flask import Flask, render_template, Response, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps

from ejercicios import *
from svg.generarSVG import randomSVG

# -----------------------------------------------------------------------------
# INICIO DE LA APP
# -----------------------------------------------------------------------------

app = Flask(__name__)

# -----------------------------------------------------------------------------
# BASE DE DATOS
# -----------------------------------------------------------------------------

client = MongoClient("mongo", 27017)
db = client.cockteles

# -----------------------------------------------------------------------------
# ROUTE HOME
# -----------------------------------------------------------------------------

# Página principal
@app.route('/')
def routeHome():
    return render_template("index.html")

# -----------------------------------------------------------------------------
# ROUTES P1
# -----------------------------------------------------------------------------

# Ejercicio criba de Eratóstenes
@app.route('/criba/<int:valor>/')
def routeCriba(valor):
    return cribaEratostenes(valor)

# Ejercicio sucesión de Fibonacci
@app.route('/fibonacci/<int:valor>/')
def routeFibonacci(valor):
    return str(Fibonacci(valor))

# Ejercicio cadena de corchetes
@app.route('/cadena/<string:cadena>/')
def routeCadena(cadena):
    if cadenaCorrecta(cadena):
        return 'La cadena es correcta'
    else:
        return 'La cadena es incorrecta'

# Ejercicio expresiones regulares
@app.route('/eregulares/<string:cadena>/')
def routeEregulares(cadena):
    if identificarPalabra(cadena):
        return 'Es una palabra + espacio + mayúscula'
    else:
        if identificarCorreo(cadena):
            return 'Es un correo'
        else:
            if identificarTarjeta(cadena):
                return 'Es una tarjeta'
            else:
                return 'No es algo que pueda identificar'

# Ejercicio de mostrar una imagen
@app.route('/imagen/')
def routeImagen():
    return render_template("imagen.html")

# Ejercicio de error 404 : URL no definida
@app.errorhandler(404)
def routePageNotFound(e):
    return render_template("404.html"), 404

# Ejercicio de imágenes dinámicas
@app.route('/svg/')
def routeSvg():
    randomsvg = randomSVG()
    return '<h1>Random SVG<br/></h1>'+''.join(randomsvg)

# -----------------------------------------------------------------------------
# ROUTES P2.1
# -----------------------------------------------------------------------------

@app.route('/todas_recetas/')
def routeRecetas():
    lista_recetas = []
    recetas = db.recipes.find()                                                                    # devuelve un cursor(*), no una lista ni un iterador
    
    for receta in recetas:
        app.logger.debug(receta)                                                                   # salida consola
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')

@app.route('/recetas_de/<string:elemento>/')
def routeRecetasDe(elemento):
    lista_recetas = []
    recetas = db.recipes.find({ "name": {"$regex": elemento, "$options": 'i'} })

    for receta in recetas:
        app.logger.debug(receta)
        lista_recetas.append(receta)
    
    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    resJson = dumps(response)
    return Response(resJson, mimetype='application/json')

@app.route('/recetas_con/<string:elemento>/')
def routeRecetasCon(elemento):
    lista_recetas = []
    recetas = db.recipes.find({ "ingredients.name": {"$regex": elemento, "$options":'i'} })

    for receta in recetas:
        app.logger.debug(receta)
        lista_recetas.append(receta)
    
    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    resJson = dumps(response)
    return Response(resJson, mimetype='application/json')

@app.route('/recetas_compuestas_de/<int:numero>/ingredientes/')
def routeRecetasCompuestas(numero):
    lista_recetas = []
    recetas = db.recipes.find({ "ingredients": {"$size": numero} })

    for receta in recetas:
        app.logger.debug(receta)
        lista_recetas.append(receta)
    
    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    resJson = dumps(response)
    return Response(resJson, mimetype='application/json')
