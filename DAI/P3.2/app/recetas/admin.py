# videogameStore/admin.py
from django.contrib import admin
from .models import Receta, Ingrediente

admin.site.register(Receta)
admin.site.register(Ingrediente)