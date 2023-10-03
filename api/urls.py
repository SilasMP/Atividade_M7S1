from django.urls import path
from api.views import *

app_name = 'api'
urlpatterns = [
    path('categorias/', mostrar_categorias, name='categorias_api'),
    path('noticias/', mostrar_noticias, name='noticias_api'),
    path('adicionar-categoria/', adicionar_categoria, name='adicionar_categoria'),
    path('adicionar-noticia/', adicionar_noticia, name='adicionar_noticia'),
]