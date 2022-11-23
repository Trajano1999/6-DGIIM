from django.shortcuts import render, redirect, get_object_or_404
from .models import Receta
from .forms import RecetaForm

# jjj Cosas por hacer:
#   1. Añadir ingredientes a la búsqueda, no solo recetas.
#   2. Almacenar las fotos en forms.py.
#   3. Eliminar recetas.
#   4. Mensajes de creación y edición.

def index(request):
    if request.GET.get('searchInput') != None:
        busquedas = Receta.objects.filter(nombre = request.GET.get('searchInput')) 
    else:
        busquedas = Receta.objects.all()
    return render(request, "index.html", {'busquedas': busquedas})

def detalles(request, id):
    receta = Receta.objects.get(pk = id)
    return render(request, "detalles.html", {'receta': receta})

def nueva_receta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.instance
            receta.save()
            return redirect('index')   # jjj podemos poner redirect('detalles', id=receta.id) si queremos que nos lleve al detalle de la nueva receta.
    else:
        form = RecetaForm()
    return render(request, 'nueva_receta.html', {'form': form})

def editar_receta(request, id):
    receta = get_object_or_404(Receta, id=id)
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES, instance=receta)
        if form.is_valid():
            receta = form.instance
            receta.save()
            return redirect('detalles', id=receta.id)
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'nueva_receta.html', {'form': form})