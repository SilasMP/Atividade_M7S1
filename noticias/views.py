from django.shortcuts import render
from noticias.models import Noticias
from noticias.forms import NoticiaForm

def publicar_noticia(request):
    sucesso = False
    form = NoticiaForm(request.POST or None)
    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'form': form,
        'sucesso': sucesso,
    }
    return render(request, 'pub_noticia.html', contexto)