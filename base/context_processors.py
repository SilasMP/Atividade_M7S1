from base.models import Categorias

def menu_categorias(request):
    menu = Categorias.objects.all()
    return {'categorias': menu}