from django.core.exceptions import ValidationError
from django.db import models

from .mesa import Mesa
from .plato import Plato
from .mesero import Mesero
from .cliente import Cliente


class DetalleOrden(models.Model):
    orden = models.ForeignKey('Orden', on_delete=models.CASCADE)
    plato = models.ForeignKey('Plato', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad}x {self.plato.nombre}"


class Orden(models.Model):
    ESTADO_CHOICES = (
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
    )

    platos = models.ManyToManyField('Plato', through='DetalleOrden')
    mesero = models.ForeignKey('Mesero', on_delete=models.CASCADE)
    mesa = models.ForeignKey('Mesa', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='abierto')
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden {self.id} - Mesa {self.mesa.numero}"

    def save(self, *args, **kwargs):
        if self.estado == 'abierto':
            conflictos = Orden.objects.filter(
                mesa=self.mesa,
                estado='abierto'
            ).exclude(id=self.id)

            if conflictos.exists():
                raise ValidationError("La mesa ya tiene una orden abierta")
        super().save(*args, **kwargs)
