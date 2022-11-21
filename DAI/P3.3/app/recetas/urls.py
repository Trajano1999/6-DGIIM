from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recetas/<int:id>/', views.detalles, name='detalles'),
    path('receta/new', views.nueva_receta, name='nueva_receta'),
]