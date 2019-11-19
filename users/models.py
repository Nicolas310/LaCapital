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

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    def __str__(self):
        return self.title