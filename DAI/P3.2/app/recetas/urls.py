from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receta/<int:id>/', views.detalles, name='detalles'),
]