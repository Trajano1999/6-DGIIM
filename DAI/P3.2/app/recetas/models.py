# ¡ al modificar este archivo debemos migrar !

from django.db import models
  
class Receta(models.Model):
  nombre       = models.CharField(max_length=200)
  preparación  = models.TextField(max_length=5000)
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