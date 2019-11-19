from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Corte/Carne/<int:pk>/', views.detalle, name='detalle'),
    path('Corte/Nuevo', views.nuevo, name='nuevo'),
    path('Registrarse', views.registro, name='registro'),
]