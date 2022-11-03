import re
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "inicio.html", {})

def detalles(request):
    return render(request, "detalles.html", {})

'''
def busqueda(request):
    return render(request, , {})
'''