from django import forms
from ..models.lbi import LBIIndicador

class LBIForm(forms.ModelForm):
    class Meta:
        model = LBIIndicador
        exclude = ['criado_por', 'atualizado_por', 'data_criacao', 'data_atualizacao']
        widgets = {
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'mes': forms.Select(attrs={'class': 'form-control'}),
            'satelite': forms.NumberInput(attrs={'class': 'form-control'}),
            'cabo_fibra_optica': forms.NumberInput(attrs={'class': 'form-control'}),
            'feixe_hertziano': forms.NumberInput(attrs={'class': 'form-control'}),
            'disponivel_nominal_down': forms.NumberInput(attrs={'class': 'form-control'}),
            'instalada_equipada_down': forms.NumberInput(attrs={'class': 'form-control'}),
            'contratada_down': forms.NumberInput(attrs={'class': 'form-control'}),
            'utilizada_down': forms.NumberInput(attrs={'class': 'form-control'}),
            'disponivel_nominal_up': forms.NumberInput(attrs={'class': 'form-control'}),
            'instalada_equipada_up': forms.NumberInput(attrs={'class': 'form-control'}),
            'contratada_up': forms.NumberInput(attrs={'class': 'form-control'}),
            'utilizada_up': forms.NumberInput(attrs={'class': 'form-control'}),
        }