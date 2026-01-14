from django.db import models

class Gasto(models.Model):
    descricao = models.CharField(max_length=120)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=60)
    concluido = models.BooleanField(default=False)  # ✅ pago/concluído
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ ordenação

    def __str__(self):
        return f"{self.descricao} - {self.valor}"
