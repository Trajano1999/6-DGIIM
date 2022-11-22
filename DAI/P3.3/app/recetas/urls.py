from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recetas/<int:id>/', views.detalles, name='detalles'),
    path('recetas/new/', views.nueva_receta, name='nueva_receta'),
    path('recetas/edit/<int:id>/', views.editar_receta, name='editar_receta'),
]