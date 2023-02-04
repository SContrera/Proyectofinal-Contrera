from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class MasculinaS(models.Model):
    
      
      nombre=models.CharField(max_length=50)
      fragancia=models.CharField(max_length=200)
      tamanio = models.CharField(max_length=10)
      autor= models.CharField(max_length=30)
      precio=models.CharField(max_length=30)
      fecha=models.DateField()
      detalles=models.TextField(200)

      def __str__(self):
             return f"Nombre: {self.nombre} - Fragancia {self.fragancia}"


    
class FemeninaS(models.Model):
    
      
      nombre=models.CharField(max_length=50)
      fragancia=models.CharField(max_length=200)
      tamanio = models.CharField(max_length=10)
      autor= models.CharField(max_length=30)
      precio=models.CharField(max_length=30)
      fecha=models.DateField()
      detalles=models.TextField(200)
      
      def __str__(self):
             return f"Nombre: {self.nombre} - Fragancia {self.fragancia}"
      


class InfantileS(models.Model):
    
      
      nombre=models.CharField(max_length=50)
      fragancia=models.CharField(max_length=200)
      tamanio = models.CharField(max_length=10)
      autor= models.CharField(max_length=30)
      precio=models.CharField(max_length=30)
      fecha=models.DateField()
      detalles=models.TextField(200)

      def __str__(self):
             return f"Nombre: {self.nombre} - Fragancia {self.fragancia}"


class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

