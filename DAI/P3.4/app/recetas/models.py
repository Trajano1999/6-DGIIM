# ¡ Al modificar los campos de este archivo debemos migrar !

from django.db import models
from .validators import validate_mayus

class Receta(models.Model):
	nombre       = models.CharField(max_length=200, validators=[validate_mayus])
	preparación  = models.TextField(max_length=5000, validators=[validate_mayus])
	foto         = models.FileField(upload_to='media/fotos')
  
	def __str__(self):
		return self.nombre
  
class Ingrediente(models.Model):
	nombre        = models.CharField(max_length=100)
	cantidad      = models.PositiveSmallIntegerField()
	unidades      = models.CharField(max_length=5)
	receta        = models.ForeignKey(Receta, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre