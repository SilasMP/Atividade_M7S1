from django.urls import path
from noticias.views import publicar_noticia

app_name = 'noticias'
urlpatterns = [
    path('publicar/', publicar_noticia, name='publicar'),
]