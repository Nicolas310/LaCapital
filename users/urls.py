from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Corte/Vendidos', views.vendido, name='vendido'),
    path('Corte/Carne/<int:pk>/', views.detalle, name='detalle'),
    path('Corte/Nuevo', views.nuevo, name='nuevo'),
    path('Registrarse', views.registro, name='registro'),
    path('Corte/Carne/<int:pk>/Editar/', views.editar, name='editar'),
    path('Corte/Carne/<int:pk>/Comprar/', views.comprar, name='comprar'),
]