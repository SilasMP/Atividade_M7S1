from django.urls import path
from api.views import CategoriasViewSet
from rest_framework.routers import DefaultRouter

from api.views import *

app_name = 'api'

router = DefaultRouter(trailing_slash=False)
router.register('categorias', CategoriasViewSet, basename='categorias')
router.register('noticias', NoticiasViewSet, basename='noticias')
urlpatterns = []
urlpatterns += router.urls