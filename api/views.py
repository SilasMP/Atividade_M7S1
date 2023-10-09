from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Categorias
from noticias.models import Noticias

from rest_framework.viewsets import ModelViewSet
from api.serializers import CategoriasSerializer, NoticiasSerializer

class CategoriasViewSet(ModelViewSet):
    serializer_class = CategoriasSerializer
    queryset = Categorias.objects.all()

class NoticiasViewSet(ModelViewSet):
    serializer_class = NoticiasSerializer
    queryset = Noticias.objects.all()