from django import forms
from ..models.trafego_originado import TrafegoOriginadoIndicador

class TrafegoOriginadoForm(forms.ModelForm):
    class Meta:
        model = TrafegoOriginadoIndicador
        exclude = ['criado_por', 'atualizado_por', 'data_criacao', 'data_atualizacao']
        widgets = {
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'mes': forms.Select(attrs={'class': 'form-control'}),
            'trafego_dados_3g_upgrade': forms.NumberInput(attrs={'class': 'form-control'}),
            'internet_3g': forms.NumberInput(attrs={'class': 'form-control'}),
            'internet_3g_placas_modem': forms.NumberInput(attrs={'class': 'form-control'}),
            'internet_3g_modem_usb': forms.NumberInput(attrs={'class': 'form-control'}),
            'trafego_dados_4g': forms.NumberInput(attrs={'class': 'form-control'}),
            'internet_4g': forms.NumberInput(attrs={'class': 'form-control'}),
            'internet_4g_placas_modem': forms.NumberInput(attrs={'class': 'form-control'}),
            'internet_4g_modem_usb': forms.NumberInput(attrs={'class': 'form-control'}),
            'trafego_dados_2g': forms.NumberInput(attrs={'class': 'form-control'}),
            'trafego_dados_3g_upgrade_sessoes': forms.NumberInput(attrs={'class': 'form-control'}),
            'internet_3g_sessoes': forms.NumberInput(attrs={'class': 'form-control'}),
            'internet_3g_placas_modem_sessoes': forms.NumberInput(attrs={'class': 'form-control'}),
            'internet_3g_modem_usb_sessoes': forms.NumberInput(attrs={'class': 'form-control'}),
            'sms_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'sms_on_net': forms.NumberInput(attrs={'class': 'form-control'}),
            'sms_off_net': forms.NumberInput(attrs={'class': 'form-control'}),
            'sms_internacional': forms.NumberInput(attrs={'class': 'form-control'}),
            'sms_cedeao': forms.NumberInput(attrs={'class': 'form-control'}),
            'sms_palop': forms.NumberInput(attrs={'class': 'form-control'}),
            'sms_cplp': forms.NumberInput(attrs={'class': 'form-control'}),
            'sms_resto_africa': forms.NumberInput(attrs={'class': 'form-control'}),
            'sms_resto_mundo': forms.NumberInput(attrs={'class': 'form-control'}),
            'voz_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'voz_on_net': forms.NumberInput(attrs={'class': 'form-control'}),
            'voz_off_net': forms.NumberInput(attrs={'class': 'form-control'}),
            'voz_mtn': forms.NumberInput(attrs={'class': 'form-control'}),
            'voz_internacional': forms.NumberInput(attrs={'class': 'form-control'}),
            'voz_cedeao': forms.NumberInput(attrs={'class': 'form-control'}),
            'voz_cplp': forms.NumberInput(attrs={'class': 'form-control'}),
            'voz_palop': forms.NumberInput(attrs={'class': 'form-control'}),
            'voz_resto_africa': forms.NumberInput(attrs={'class': 'form-control'}),
            'voz_resto_mundo': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_total': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_on_net': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_off_net': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_mtn': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_internacional': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_cedeao': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_cplp': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_palop': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_resto_africa': forms.NumberInput(attrs={'class': 'form-control'}),
            'chamadas_resto_mundo': forms.NumberInput(attrs={'class': 'form-control'}),
            'operador_movel_b': forms.NumberInput(attrs={'class': 'form-control'}),
            'operador_rede_fixa': forms.NumberInput(attrs={'class': 'form-control'}),
            'numeros_curtos': forms.NumberInput(attrs={'class': 'form-control'}),
        }