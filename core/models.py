from django.db import models
from recursos.models import Recursos

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    recursos = models.ManyToManyField(Recursos)

    def __str__(self):
        return self.nome