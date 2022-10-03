from email.policy import default
from django.db import models

# Create your models here.
class Productos(models.Model):
    id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    contenido_neto=models.IntegerField(default=0)
    precio=models.IntegerField(default=0)
    descripcion=models.CharField(max_length=200, blank=True)