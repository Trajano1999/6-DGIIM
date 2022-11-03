from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalles/', views.detalles, name='detalles'),
    path('<string>/', views.busqueda, name='busqueda')),
]