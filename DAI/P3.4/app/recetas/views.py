from django.shortcuts import render, redirect, get_object_or_404
from .models import Receta
from .forms import RecetaForm
from django.contrib import messages

# jjj Cosas por hacer:
#   1. Estilizar mensajes de creación y edición.
#   2. Ventana modal al borrar.
#   3. Validación de campos.
#   4. Añadir ingredientes a la búsqueda, no solo recetas.

def index(request):
    if request.GET.get('searchInput') != None:
        busquedas = Receta.objects.filter(nombre = request.GET.get('searchInput')) 
    else:
        busquedas = Receta.objects.all()
    return render(request, "index.html", {'busquedas': busquedas})

def detalles(request, id):
    receta = Receta.objects.get(id = id)
    return render(request, "detalles.html", {'receta': receta})

def nueva_receta(request):
    if request.method == "POST":
        form = RecetaForm(request.POST, request.FILES)
        if form.is_valid():
            receta = form.instance
            receta.save()
            messages.add_message(request, messages.SUCCESS, 'Nueva receta creada!')
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
            messages.add_message(request, messages.SUCCESS, 'Receta editada!')
            return redirect('detalles', id=receta.id)
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'nueva_receta.html', {'form': form})

def eliminar(request, id):
    receta = Receta.objects.get(id = id)
    receta.delete()
    messages.add_message(request, messages.SUCCESS, 'Receta eliminada!')
    return redirect('index')