from django import forms
from ..models.trafego_internet import TrafegoInternetIndicador

class TrafegoInternetForm(forms.ModelForm):
    class Meta:
        model = TrafegoInternetIndicador
        exclude = ['criado_por', 'atualizado_por', 'data_criacao', 'data_atualizacao']
        widgets = {
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'mes': forms.Select(attrs={'class': 'form-control'}),
            'trafego_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'por_via_satelite': forms.NumberInput(attrs={'class': 'form-control'}),
            'por_sistema_hertziano_fixo_terra': forms.NumberInput(attrs={'class': 'form-control'}),
            'fibra_otica': forms.NumberInput(attrs={'class': 'form-control'}),
            'banda_estreita_256kbps': forms.NumberInput(attrs={'class': 'form-control'}),
            'kbps_64_128': forms.NumberInput(attrs={'class': 'form-control'}),
            'kbps_128_256': forms.NumberInput(attrs={'class': 'form-control'}),
            'banda_estreita_outros': forms.NumberInput(attrs={'class': 'form-control'}),
            'banda_larga_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'kbits_256_2mbits': forms.NumberInput(attrs={'class': 'form-control'}),
            'mbits_2_4': forms.NumberInput(attrs={'class': 'form-control'}),
            'mbits_10': forms.NumberInput(attrs={'class': 'form-control'}),
            'banda_larga_outros': forms.NumberInput(attrs={'class': 'form-control'}),
            'residencial': forms.NumberInput(attrs={'class': 'form-control'}),
            'corporativo_empresarial': forms.NumberInput(attrs={'class': 'form-control'}),
            'instituicoes_publicas': forms.NumberInput(attrs={'class': 'form-control'}),
            'instituicoes_ensino': forms.NumberInput(attrs={'class': 'form-control'}),
            'instituicoes_saude': forms.NumberInput(attrs={'class': 'form-control'}),
            'ong_outros': forms.NumberInput(attrs={'class': 'form-control'}),
            'cidade_bissau': forms.NumberInput(attrs={'class': 'form-control'}),
            'bafata': forms.NumberInput(attrs={'class': 'form-control'}),
            'biombo': forms.NumberInput(attrs={'class': 'form-control'}),
            'bolama_bijagos': forms.NumberInput(attrs={'class': 'form-control'}),
            'cacheu': forms.NumberInput(attrs={'class': 'form-control'}),
            'gabu': forms.NumberInput(attrs={'class': 'form-control'}),
            'oio': forms.NumberInput(attrs={'class': 'form-control'}),
            'quinara': forms.NumberInput(attrs={'class': 'form-control'}),
            'tombali': forms.NumberInput(attrs={'class': 'form-control'}),
            'acesso_livre': forms.NumberInput(attrs={'class': 'form-control'}),
            'acesso_condicionado': forms.NumberInput(attrs={'class': 'form-control'}),
        }