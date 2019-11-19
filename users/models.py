from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    TIPO = (
        ('ADMINISTRADOR','ADMINISTRADOR'),
        ('COMPRADOR','COMPRADOR'),
    )
    tipo = models.CharField(max_length=80,choices=TIPO,default='COMPRADOR')

class Carnes(models.Model):
    TIPO = (
        ('POLLO ENTERO','POLLO ENTERO'),
        ('POLLO BISTEC','POLLO BISTEC'),
        ('POLLO TRUTRO LARGO','POLLO TRUTRO LARGO'),
        ('POLLO TRUTRO CORTO','POLLO TRUTRO CORTO'),
        ('PLATEADA CERDO','PLATEADA CERDO'),
        ('SOBRECOSTILLA','SOBRECOSTILLA'),
        ('LOMO LISO','LOMO LISO'),
        ('Asado Carnicero,','Asado Carnicero,'),
    )
    tipo = models.CharField(max_length=80,choices=TIPO,default='POLLO ENTERO')
    ESTADO = (
        ('DISPONIBLE','DISPONIBLE'),
        ('VENDIDO','VENDIDO'),
    )
    estado = models.CharField(max_length=80,choices=ESTADO,default='DISPONIBLE')
    titulo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio_kilo = models.IntegerField()
    peso = models.IntegerField()
    precio_total = models.IntegerField()
    def __str__(self):
        return self.titulo