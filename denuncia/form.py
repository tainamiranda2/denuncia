from django import forms

from .models import Denuncia

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ('nome', 'cpf','descricao', 'celular', 'endereco', 'status_denuncia')

        widgets = {
                    'status_denuncia': forms.Select(attrs={'class': 'form-select'}),
                    'nome': forms.TextInput(attrs={'class': 'form-control'}),
                'cpf': forms.TextInput(attrs={'class': 'form-control'}),
                'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
                'celular': forms.TextInput(attrs={'class': 'form-control'}),
                'endereco': forms.TextInput(attrs={'class': 'form-control'}),
                }