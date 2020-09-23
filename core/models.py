from django.db import models
from classificacao.models import Classificacao

class Viagem(models.Model):
    dt_inicio = models.DateField()
    dt_fim = models.DateField()
    classificacao = models.ForeignKey(
            Classificacao, on_delete=models.CASCADE, null=True, blank=True)
    nota = models.DecimalField(decimal_places=2, max_digits=3)

    def __str__(self):
        return self.classificacao
    