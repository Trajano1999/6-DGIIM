from django.shortcuts import render, redirect
from .models import Receta
from .forms import RecetaForm

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
            return redirect('detalles', id=receta.id)   # jjj podemos poner redirect('index') si queremos que nos lleve a la pagina principal
    else:
        form = RecetaForm()

    return render(request, 'nueva_receta.html', {'form': form})