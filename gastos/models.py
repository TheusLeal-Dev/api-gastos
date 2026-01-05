from django.db import models

# Create your models here.

from django.db import models

class Gasto(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao
