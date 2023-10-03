from django import forms
from noticias.models import Noticias
from base.models import Categorias

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = ['titulo', 'categoria', 'descricao']
        widgets = {
            'titulo': forms.TextInput(
                attrs = {
                    'placeholder':'Informe o Titulo da Noticia'
                }
            ),
            'descricao': forms.Textarea(
                attrs = {
                    'placeholder':'Escreva aqui o conteúdo da Noticia'
                }
            ),
        }
   