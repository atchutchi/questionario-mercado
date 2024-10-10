# admin.py
from django.contrib import admin
from .models.estacoes_moveis import EstacoesMoveisIndicador
from .models.trafego_originado import TrafegoOriginadoIndicador
from .models.trafego_terminado import TrafegoTerminadoIndicador
from .models.trafego_roaming_internacional import TrafegoRoamingInternacionalIndicador
from .models.lbi import LBIIndicador
from .models.trafego_internet import TrafegoInternetIndicador
from .models import InternetFixoIndicador

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

@admin.register(TrafegoRoamingInternacionalIndicador)
class TrafegoRoamingInternacionalIndicadorAdmin(admin.ModelAdmin):
    list_display = ['ano', 'mes', 'criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    list_filter = ['ano', 'mes']
    search_fields = ['ano', 'mes']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']

@admin.register(LBIIndicador)
class LBIIndicadorAdmin(admin.ModelAdmin):
    list_display = ['ano', 'mes', 'criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    list_filter = ['ano', 'mes']
    search_fields = ['ano', 'mes']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']

@admin.register(TrafegoInternetIndicador)
class TrafegoInternetIndicadorAdmin(admin.ModelAdmin):
    list_display = ['ano', 'mes', 'trafego_total', 'banda_larga_total', 'criado_por', 'data_criacao']
    list_filter = ['ano', 'mes']
    search_fields = ['ano', 'mes']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    fieldsets = (
        ('Informações Gerais', {
            'fields': ('ano', 'mes')
        }),
        ('Tráfego de Serviços de Internet fixo via rádio', {
            'fields': ('trafego_total', 'por_via_satelite', 'por_sistema_hertziano_fixo_terra', 'fibra_otica')
        }),
        ('Tráfego por débito', {
            'fields': ('banda_estreita_256kbps', 'kbps_64_128', 'kbps_128_256', 'banda_estreita_outros')
        }),
        ('Banda Larga ≥ 256 Kbps', {
            'fields': ('banda_larga_total', 'kbits_256_2mbits', 'mbits_2_4', 'mbits_10', 'banda_larga_outros')
        }),
        ('Tráfego por categoria', {
            'fields': ('residencial', 'corporativo_empresarial', 'instituicoes_publicas', 'instituicoes_ensino', 'instituicoes_saude', 'ong_outros')
        }),
        ('Tráfego por Região', {
            'fields': ('cidade_bissau', 'bafata', 'biombo', 'bolama_bijagos', 'cacheu', 'gabu', 'oio', 'quinara', 'tombali')
        }),
        ('Tráfego por acesso público via rádio (PWLAN)', {
            'fields': ('acesso_livre', 'acesso_condicionado')
        }),
        ('Metadados', {
            'fields': ('criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.criado_por = request.user
        obj.atualizado_por = request.user
        super().save_model(request, obj, form, change)

@admin.register(InternetFixoIndicador)
class InternetFixoIndicadorAdmin(admin.ModelAdmin):
    list_display = ['ano', 'mes', 'cidade_bissau', 'bafata', 'biombo', 'criado_por', 'data_criacao']
    list_filter = ['ano', 'mes']
    search_fields = ['ano', 'mes', 'cidade_bissau', 'bafata', 'biombo']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    fieldsets = (
        ('Informações Gerais', {
            'fields': ('ano', 'mes')
        }),
        ('Número de assinantes de Internet fixo via rádio', {
            'fields': ('cidade_bissau', 'bafata', 'biombo', 'bolama_bijagos', 'cacheu', 'gabu', 'oio', 'quinara', 'tombali')
        }),
        ('Número de assinantes activos de Internet Fixo via Rádio', {
            'fields': ('airbox', 'sistema_hertziano_fixo_terra', 'outros_proxim', 'fibra_otica')
        }),
        ('Número de assinantes de Serviços de Internet por débito', {
            'fields': ('banda_larga_256kbits_2mbits', 'banda_larga_2_4mbits', 'banda_larga_5_10mbits', 'banda_larga_outros')
        }),
        ('Número de assinantes de Internet por categoria', {
            'fields': ('residencial', 'corporativo_empresarial', 'instituicoes_publicas', 'instituicoes_ensino', 'instituicoes_saude', 'ong_outros')
        }),
        ('Metadados', {
            'fields': ('criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.criado_por = request.user
        obj.atualizado_por = request.user
        super().save_model(request, obj, form, change)