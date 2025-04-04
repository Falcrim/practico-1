from django.db import models



class Mesa(models.Model):
    numero = models.PositiveIntegerField()

    def __str__(self):
        return str(self.numero)