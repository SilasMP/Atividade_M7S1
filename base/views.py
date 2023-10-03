from django.shortcuts import render
from base.models import Contato
from base.forms import ContatoForm
from noticias.models import Noticias

def inicio(request):
    noticias = Noticias.objects.all()
    qtda_noticias = len(noticias)
    print(qtda_noticias)
    contexto = {
        'qtda_noticias': qtda_noticias,
        'noticias': noticias,
    }

    return render(request,'index.html', contexto)

def contato(request):
    sucesso = False
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'form': form,
        'sucesso': sucesso,
    }
    return render(request, 'contato.html', contexto)    