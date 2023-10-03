from django import forms
from base.models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'prioridade', 'mensagem']
        widgets = {
            'nome': forms.TextInput(
                attrs= {
                    'placeholder':'Informe o nome Completo'
                }
            ),
            'email': forms.TextInput(
                attrs= {
                    'placeholder':'Informe o E-mail'
                }
            ),
            'mensagem': forms.Textarea(
                attrs= {
                    'placeholder':'Insira a Mensagem'
                }
            ),
        }
