from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from .base import IndicadorBase
import json

class InvestimentoIndicador(IndicadorBase):
    # Investimento Corpóreo
    # Serviços de telecomunicações
    servicos_telecomunicacoes = models.DecimalField(
        max_digits=15, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Serviços de Telecomunicações"
    )
    
    # Serviços de Internet
    servicos_internet = models.DecimalField(
        max_digits=15, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Serviços de Internet"
    )

    # Investimento Incorpóreo
    # Serviços de telecomunicações
    servicos_telecomunicacoes_incorporeo = models.DecimalField(
        max_digits=15, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Serviços de Telecomunicações (Incorpóreo)"
    )

    # Serviços de Internet
    servicos_internet_incorporeo = models.DecimalField(
        max_digits=15, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Serviços de Internet (Incorpóreo)"
    )

    # Campos para rastreamento
    criado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='investimento_criado'
    )
    atualizado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='investimento_atualizado'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    # Campos adicionais dinâmicos
    outros_investimentos = models.TextField(
        null=True,
        blank=True,
        help_text="Campos adicionais de investimentos"
    )

    def calcular_total_corporeo(self):
        return self.servicos_telecomunicacoes + self.servicos_internet

    def calcular_total_incorporeo(self):
        return self.servicos_telecomunicacoes_incorporeo + self.servicos_internet_incorporeo

    def calcular_total_geral(self):
        return self.calcular_total_corporeo() + self.calcular_total_incorporeo()

    def calcular_total_outros(self):
        outros = self.get_outros_investimentos()
        if not outros:
            return 0
        return sum(float(valor) for valor in outros.values())
        
    def get_outros_investimentos(self):
        """Retorna os outros investimentos como dicionário."""
        if not self.outros_investimentos:
            return {}
        try:
            return json.loads(self.outros_investimentos)
        except json.JSONDecodeError:
            return {}
            
    def set_outros_investimentos(self, investimentos):
        """Define os outros investimentos."""
        self.outros_investimentos = json.dumps(investimentos)

    def __str__(self):
        return f"Investimento - {self.ano}/{self.mes} - {self.get_operadora_display()}"

    class Meta:
        unique_together = ('ano', 'mes', 'operadora')
        verbose_name = "Indicador de Investimento"
        verbose_name_plural = "Indicadores de Investimento"