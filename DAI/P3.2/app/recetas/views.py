from django.shortcuts import render
from recetas.models import Receta

def index(request):
    if request.GET.get('searchInput') != None:
        busquedas = Receta.objects.filter(nombre = request.GET.get('searchInput'))
        return render(request, 'lista_recetas.html', {'busquedas': busquedas})
    else:
        busquedas = Receta.objects.all()
        return render(request, "index.html", {'busquedas': busquedas})

def detalles(request, id):
    receta = Receta.objects.get(pk = id)
    return render(request, "detalles.html", {'receta': receta})
