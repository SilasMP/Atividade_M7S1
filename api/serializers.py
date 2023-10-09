from rest_framework.serializers import ModelSerializer
from base.models import Categorias
from noticias.models import Noticias

class CategoriasSerializer(ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'

class NoticiasSerializer(ModelSerializer):
    class Meta:
        model = Noticias
        fields = '__all__'