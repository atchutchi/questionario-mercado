from django.db import models
from django.conf import settings
from .base import IndicadorBase

class EstacoesMoveisIndicador(IndicadorBase):
    # Serviços de Mobile Money
    numero_utilizadores = models.IntegerField()
    numero_utilizadores_mulher = models.IntegerField()
    numero_utilizadores_homem = models.IntegerField()

    total_carregamentos = models.DecimalField(max_digits=20, decimal_places=2)
    total_carregamentos_mulher = models.DecimalField(max_digits=20, decimal_places=2)
    total_carregamentos_homem = models.DecimalField(max_digits=20, decimal_places=2)

    total_levantamentos = models.DecimalField(max_digits=20, decimal_places=2)
    total_levantamentos_mulher = models.DecimalField(max_digits=20, decimal_places=2)
    total_levantamentos_homem = models.DecimalField(max_digits=20, decimal_places=2)

    total_transferencias = models.DecimalField(max_digits=20, decimal_places=2)
    total_transferencias_mulher = models.DecimalField(max_digits=20, decimal_places=2)
    total_transferencias_homem = models.DecimalField(max_digits=20, decimal_places=2)

    # Utilizadores de serviço
    sms = models.IntegerField()
    mms = models.IntegerField(null=True, blank=True)
    mobile_tv = models.IntegerField(null=True, blank=True)
    roaming_internacional_out_parc_roaming_out = models.IntegerField()
    banda_larga_movel = models.IntegerField()
    utilizadores_5g_upgrades = models.IntegerField()
    utilizadores_servico_acesso_internet_banda_larga = models.IntegerField()
    utilizadores_placas_box = models.IntegerField()
    utilizadores_placas_usb = models.IntegerField()
    utilizadores_servico_4g = models.IntegerField()

    # Número total de estações móveis activos
    afectos_planos_pos_pagos = models.IntegerField()
    afectos_planos_pos_pagos_utilizacao = models.IntegerField()
    afectos_planos_pre_pagos = models.IntegerField()
    afectos_planos_pre_pagos_utilizacao = models.IntegerField()
    associados_situacoes_especificas = models.IntegerField(null=True, blank=True)
    outros_residuais = models.IntegerField(null=True, blank=True)

    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='estacoes_moveis_criadas')
    atualizado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='estacoes_moveis_atualizadas')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def calcular_total_utilizadores(self):
        return self.numero_utilizadores

    def calcular_total_carregamentos(self):
        return self.total_carregamentos

    def calcular_total_levantamentos(self):
        return self.total_levantamentos

    def calcular_total_transferencias(self):
        return self.total_transferencias

    def calcular_total_estacoes_moveis(self):
        return (self.afectos_planos_pos_pagos + 
                self.afectos_planos_pre_pagos + 
                (self.associados_situacoes_especificas or 0) + 
                (self.outros_residuais or 0))

    def str(self):
        return f"Estações Móveis e Mobile Money - {self.ano}/{self.mes}"

    class Meta:
        unique_together = ('ano', 'mes')