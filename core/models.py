from django.db import models
from recursos.models import Recurso
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    recursos = models.ManyToManyField(Recurso)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)

    def __str__(self):
        return self.nome