from django.db import models

ESCOLHA = [
    ('alta', 'Alta'),
    ('media', 'Média'),
    ('baixa', 'Baixa'),
]

class TimeStampedModel(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Contato(TimeStampedModel):
    nome = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail')
    prioridade = models.CharField('Prioridade', max_length=6,  choices=ESCOLHA)
    mensagem = models.TextField('Mensagem')
    lido = models.BooleanField('Lido', default=False, blank=True)

    def __str__(self):
        return self.nome
    
class Categorias(TimeStampedModel):
    nome = models.CharField('Nome', max_length=50)
    descricao = models.CharField('Descrição', max_length=300)

    def __str__(self):
        return self.nome