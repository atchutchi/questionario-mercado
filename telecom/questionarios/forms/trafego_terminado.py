# forms/trafego_terminado.py
from django import forms
from ..models.trafego_terminado import TrafegoTerminadoIndicador

class TrafegoTerminadoForm(forms.ModelForm):
    class Meta:
        model = TrafegoTerminadoIndicador
        exclude = ['criado_por', 'atualizado_por', 'data_criacao', 'data_atualizacao']
        widgets = {
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'mes': forms.Select(attrs={'class': 'form-control'}),
            'chamadas_outros_op_moveis_nacionais': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_mtn': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_operador_b': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_outros': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_operador_rede_fixa': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_cedeao': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_cplp': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_palop': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_resto_africa': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_resto_mundo': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_numeros_curtos': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_outros_op_moveis_nacionais': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_mtn': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_operador_b': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_outros': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_operador_rede_fixa': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_cedeao': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_cplp': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_palop': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_resto_africa': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_resto_mundo': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_numeros_curtos': forms.NumberInput(attrs={'class': 'form-control'}),
            'sms_outras_redes_moveis_nacionais': forms.NumberInput(attrs={'class': 'form-control'}),
            'sms_outras_redes_internacionais': forms.NumberInput(attrs={'class': 'form-control'}),
            'sms_outros': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        # Você pode adicionar validações personalizadas aqui, se necessário
        return cleaned_data