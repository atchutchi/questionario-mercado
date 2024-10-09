from django.db import models
from django.conf import settings
from .base import IndicadorBase

class TrafegoOriginadoIndicador(IndicadorBase):
    # Tráfego de Dados 3G e upgrade
    trafego_dados_3g_upgrade = models.BigIntegerField(help_text="Em Mbit/s")
    internet_3g = models.BigIntegerField(help_text="Em Mbit")
    internet_3g_placas_modem = models.BigIntegerField(help_text="Em Mbit")
    internet_3g_modem_usb = models.BigIntegerField(help_text="Em Mbit")

    # Tráfego de Dados 4G
    trafego_dados_4g = models.BigIntegerField(help_text="Em Mbit/s")
    internet_4g = models.BigIntegerField(help_text="Em Mbyte (Mo)")
    internet_4g_placas_modem = models.BigIntegerField(help_text="Em Mbyte (Mo)")
    internet_4g_modem_usb = models.BigIntegerField(help_text="Em Mbyte (Mo)")

    # Tráfego de Dados das redes 2G
    trafego_dados_2g = models.BigIntegerField(help_text="Em Sessões")

    # Tráfego de Dados das redes 3G e upgrade
    trafego_dados_3g_upgrade_sessoes = models.BigIntegerField(help_text="Em Sessões")
    internet_3g_sessoes = models.BigIntegerField(help_text="Em Sessões")
    internet_3g_placas_modem_sessoes = models.BigIntegerField(help_text="Em Sessões")
    internet_3g_modem_usb_sessoes = models.BigIntegerField(help_text="Em Sessões")

    # Tráfego de Mensagens
    sms_total = models.BigIntegerField(help_text="Número de mensagens enviadas")
    sms_on_net = models.BigIntegerField()
    sms_off_net = models.BigIntegerField()
    sms_internacional = models.BigIntegerField()
    sms_cedeao = models.BigIntegerField()
    sms_palop = models.BigIntegerField()
    sms_cplp = models.BigIntegerField()
    sms_resto_africa = models.BigIntegerField()
    sms_resto_mundo = models.BigIntegerField()

    # Volume de Tráfegos de Voz
    voz_total = models.BigIntegerField(help_text="Em minutos")
    voz_on_net = models.BigIntegerField(help_text="Em minutos")
    voz_off_net = models.BigIntegerField(help_text="Em minutos")
    voz_mtn = models.BigIntegerField(help_text="Em minutos")
    voz_internacional = models.BigIntegerField(help_text="Em minutos")
    voz_cedeao = models.BigIntegerField(help_text="Em minutos")
    voz_cplp = models.BigIntegerField(help_text="Em minutos")
    voz_palop = models.BigIntegerField(help_text="Em minutos")
    voz_resto_africa = models.BigIntegerField(help_text="Em minutos")
    voz_resto_mundo = models.BigIntegerField(help_text="Em minutos")

    # Número de Comunicações de Voz
    chamadas_total = models.BigIntegerField(help_text="Número de chamadas")
    chamadas_on_net = models.BigIntegerField()
    chamadas_off_net = models.BigIntegerField()
    chamadas_mtn = models.BigIntegerField()
    chamadas_internacional = models.BigIntegerField()
    chamadas_cedeao = models.BigIntegerField()
    chamadas_cplp = models.BigIntegerField()
    chamadas_palop = models.BigIntegerField()
    chamadas_resto_africa = models.BigIntegerField()
    chamadas_resto_mundo = models.BigIntegerField()

    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='trafego_originado_criado')
    atualizado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='trafego_originado_atualizado')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Tráfego Originado - {self.ano}/{self.mes}"

    class Meta:
        unique_together = ('ano', 'mes')