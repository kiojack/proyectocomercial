from django.db import models
from django.utils import timezone
from decimal import Decimal

class Habitacion(models.Model):
    numero = models.CharField(max_length=200)
    capacidad= models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='photos')
    precio = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))
    estado=models.BooleanField(default=0)

    def __str__(self):
        return self.numero

class Reservar(models.Model):
    autor = models.ForeignKey('auth.User')
    habitacion = models.ForeignKey(Habitacion)
    descripcion= models.TextField()
    fechacreado = models.DateTimeField(
            default=timezone.now)
    fechainicio= models.DateTimeField(
            blank=True, null=True)
    fechafinal= models.DateTimeField(
            blank=True, null=True)
    Total = models.DecimalField(max_digits=10,decimal_places=2,default=Decimal('0.00'))

    def __str__(self):
        return self.fechacreado

    def publish(self):
        self.fechacreado = timezone.now()
        self.save()