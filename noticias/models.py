from django.db import models
from base.models import TimeStampedModel, Categorias

class Noticias(TimeStampedModel):
    titulo = models.CharField('Título', max_length=300)
    categoria  = models.ForeignKey(Categorias, on_delete=models.SET_DEFAULT, default=6)
    descricao = models.TextField('Noticia')

    def __str__(self):
        return self.titulo