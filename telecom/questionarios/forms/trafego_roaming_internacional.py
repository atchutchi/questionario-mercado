from django import forms
from ..models.trafego_roaming_internacional import TrafegoRoamingInternacionalIndicador

class TrafegoRoamingInternacionalForm(forms.ModelForm):
    class Meta:
        model = TrafegoRoamingInternacionalIndicador
        exclude = ['criado_por', 'atualizado_por', 'data_criacao', 'data_atualizacao']
        widgets = {
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'mes': forms.Select(attrs={'class': 'form-control'}),
            'chamadas_originadas_rede': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_terminadas_rede': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_originados_rede': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_terminados_rede': forms.NumberInput(attrs={'class': 'form-control'}),
            'mensagens_escritas_enviadas': forms.NumberInput(attrs={'class': 'form-control'}),
            'mensagens_escritas_recebidas': forms.NumberInput(attrs={'class': 'form-control'}),
            'sessoes_acesso_internet': forms.NumberInput(attrs={'class': 'form-control'}),
            'volume_acesso_internet': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_originadas_operador_roaming': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_terminadas_operador_roaming': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_originados_operador_roaming': forms.NumberInput(attrs={'class': 'form-control'}),
            'minutos_terminados_operador_roaming': forms.NumberInput(attrs={'class': 'form-control'}),
            'mensagens_escritas_enviadas_out': forms.NumberInput(attrs={'class': 'form-control'}),
            'sessoes_acesso_internet_out': forms.NumberInput(attrs={'class': 'form-control'}),
            'volume_acesso_internet_out': forms.NumberInput(attrs={'class': 'form-control'}),
            'acordos_roaming_internacional': forms.NumberInput(attrs={'class': 'form-control'}),
        }