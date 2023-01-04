# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------

from flask import Flask, render_template, Response, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from flask_restful import Resource, Api

# -----------------------------------------------------------------------------
# INICIO DE LA APP
# -----------------------------------------------------------------------------

app = Flask(__name__)
api = Api(app)

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

    resJson = dumps(lista_recetas)
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

# -----------------------------------------------------------------------------
# ROUTES P2.2
# -----------------------------------------------------------------------------

# para recibir una lista (GET), o añadir una receta (POST) 
@app.route('/api/recipes/', methods=['GET', 'POST'])
def api_1():
    if request.method == 'GET':
        buscados = db.recipes.find().sort('name')

        # utilizamos dumps para convertir a json y luego el Response para indicar al navegador el formato
        return Response(dumps(buscados), mimetype='application/json')

    elif request.method == 'POST':
        datos = request.get_json()
        db.recipes.insert_one(datos)

        insertado = db.recipes.find_one({}, datos)
        return Response(dumps(insertado), mimetype='application/json')
        

# para modificar una receta (PUT) o borrar una receta (DELETE)
@app.route('/api/recipes/<id>/', methods=['GET', 'PUT', 'DELETE'])
def api_2(id):
    if request.method == 'GET':
        buscado = db.recipes.find_one({'_id': ObjectId(id)})
        
        if buscado:
            return Response(dumps(buscado), mimetype='application/json')
        else:
            return Response({'error: Not found'}, mimetype='application/json'), 404
    
    elif request.method == 'PUT':
        buscado = db.recipes.find_one({'_id': ObjectId(id)})
        
        if buscado:
            datos = request.get_json()
            db.recipes.update_one({'_id': ObjectId(id)}, {'$set':datos})
            
            actualizado = db.recipes.find_one({'_id': ObjectId(id)})
            return Response(dumps(actualizado), mimetype='application/json')
        else:
            return Response({'error: Not found'}, mimetype='application/json'), 404

    elif request.method == 'DELETE':
        buscado = db.recipes.find_one({'_id': ObjectId(id)})

        if buscado:
            db.recipes.delete_one({'_id': ObjectId(id)})
            return Response(dumps(id), mimetype='application/json')
        else:
            return Response({'error: Not found'}, mimetype='application/json'), 404
