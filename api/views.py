from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Categorias
from noticias.models import Noticias

@api_view()
def mostrar_categorias(request):
    consulta = Categorias.objects.all()
    conteudo = []
    for categoria in consulta:
        info = {
            'id': categoria.id,
            'nome': categoria.nome,
            'descricao': categoria.descricao
        }
        conteudo.append(info)
    return Response(conteudo)

@api_view()
def mostrar_noticias(request):
    consulta = Noticias.objects.all()
    conteudo = []
    for noticia in consulta:
        info = {
            'id': noticia.id,
            'titulo': noticia.titulo,
            'categoria': {
                'id': noticia.categoria.id,  #buscando o id da tabela categorias
                'nome': noticia.categoria.nome, #buscando nome da tabela categorias
            },
            'criado_em': noticia.criado_em
        }
        conteudo.append(info)
    return Response(conteudo)

#POST EM CATEGORIAS
@api_view(['POST'])
def adicionar_categoria(request):
    nome = request.data['nome']
    descricao = request.data['descricao']
    categoria = Categorias.objects.create(nome = nome, descricao = descricao)
    info = {
        'id': categoria.id,
        'nome': categoria.nome,
        'descricao': categoria.descricao,
        'criado_em': categoria.criado_em
    }
    return Response(info)

#POST EM NOTICIAS
@api_view(['POST'])
def adicionar_noticia(request):
    titulo = request.data['titulo']
    descricao = request.data['descricao']
    noticias = Noticias.objects.create(titulo = titulo, descricao = descricao)
    info = {
        'id': noticias.id,
        'titulo': noticias.titulo,
        'categoria': {
            'id': noticias.categoria.id,
            'nome': noticias.categoria.nome,
        },
        'descricao': noticias.descricao,
        'criado_em': noticias.criado_em,
    }
    return Response(info)