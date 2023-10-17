from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from base.models import Categorias
from noticias.models import Noticias

from rest_framework.viewsets import ModelViewSet
from api.serializers import CategoriasSerializer, NoticiasSerializer

class CategoriasViewSet(ModelViewSet):
    serializer_class = CategoriasSerializer
    queryset = Categorias.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class NoticiasViewSet(ModelViewSet):
    serializer_class = NoticiasSerializer
    queryset = Noticias.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]