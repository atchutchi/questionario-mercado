# admin.py
from django.contrib import admin
from .models.estacoes_moveis import EstacoesMoveisIndicador
from .models.trafego_originado import TrafegoOriginadoIndicador
from .models.trafego_terminado import TrafegoTerminadoIndicador

@admin.register(EstacoesMoveisIndicador)
class EstacoesMoveisIndicadorAdmin(admin.ModelAdmin):
    list_display = ['ano', 'mes', 'criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    list_filter = ['ano', 'mes']
    search_fields = ['ano', 'mes']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']

@admin.register(TrafegoOriginadoIndicador)
class TrafegoOriginadoIndicadorAdmin(admin.ModelAdmin):
    list_display = ['ano', 'mes', 'criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    list_filter = ['ano', 'mes']
    search_fields = ['ano', 'mes']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']

@admin.register(TrafegoTerminadoIndicador)
class TrafegoTerminadoIndicadorAdmin(admin.ModelAdmin):
    list_display = ['ano', 'mes', 'criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    list_filter = ['ano', 'mes']
    search_fields = ['ano', 'mes']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']