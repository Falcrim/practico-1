from django.db import models



class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    nit = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre