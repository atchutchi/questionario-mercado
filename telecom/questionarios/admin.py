# admin.py
from django.contrib import admin
from .models.estacoes_moveis import EstacoesMoveisIndicador
from .models.trafego_originado import TrafegoOriginadoIndicador
from .models.trafego_terminado import TrafegoTerminadoIndicador
from .models.trafego_roaming_internacional import TrafegoRoamingInternacionalIndicador
from .models.lbi import LBIIndicador
from .models.trafego_internet import TrafegoInternetIndicador
from .models.internet_fixo import InternetFixoIndicador
from .models.receitas import ReceitasIndicador

@admin.register(EstacoesMoveisIndicador)
class EstacoesMoveisIndicadorAdmin(admin.ModelAdmin):
    list_display = ['operadora', 'ano', 'mes', 'criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    list_filter = ['operadora', 'ano', 'mes']
    search_fields = ['operadora', 'ano', 'mes']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']

@admin.register(TrafegoOriginadoIndicador)
class TrafegoOriginadoIndicadorAdmin(admin.ModelAdmin):
    list_display = ['operadora', 'ano', 'mes', 'criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    list_filter = ['operadora', 'ano', 'mes']
    search_fields = ['operadora', 'ano', 'mes']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']

@admin.register(TrafegoTerminadoIndicador)
class TrafegoTerminadoIndicadorAdmin(admin.ModelAdmin):
    list_display = ['operadora', 'ano', 'mes', 'criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    list_filter = ['operadora', 'ano', 'mes']
    search_fields = ['operadora', 'ano', 'mes']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']

@admin.register(TrafegoRoamingInternacionalIndicador)
class TrafegoRoamingInternacionalIndicadorAdmin(admin.ModelAdmin):
    list_display = ['operadora', 'ano', 'mes', 'criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    list_filter = ['operadora', 'ano', 'mes']
    search_fields = ['operadora', 'ano', 'mes']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']

@admin.register(LBIIndicador)
class LBIIndicadorAdmin(admin.ModelAdmin):
    list_display = ['operadora', 'ano', 'mes', 'criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    list_filter = ['operadora', 'ano', 'mes']
    search_fields = ['operadora', 'ano', 'mes']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']

@admin.register(TrafegoInternetIndicador)
class TrafegoInternetIndicadorAdmin(admin.ModelAdmin):
    list_display = ['operadora', 'ano', 'mes', 'trafego_total', 'banda_larga_total', 'criado_por', 'data_criacao']
    list_filter = ['operadora', 'ano', 'mes']
    search_fields = ['operadora', 'ano', 'mes']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    fieldsets = (
        ('Informações Gerais', {
            'fields': ('operadora', 'ano', 'mes')
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
    list_display = ['operadora', 'ano', 'mes', 'cidade_bissau', 'bafata', 'biombo']
    list_filter = ['operadora', 'ano', 'mes']
    search_fields = ['operadora', 'ano', 'mes', 'cidade_bissau', 'bafata', 'biombo']
    fieldsets = (
        ('Informações Gerais', {
            'fields': ('operadora', 'ano', 'mes')
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
    )


@admin.register(ReceitasIndicador)
class ReceitasIndicadorAdmin(admin.ModelAdmin):
    list_display = ['operadora', 'ano', 'mes', 
                   'calcular_total_receitas_retalhistas', 
                   'calcular_total_receitas_grossistas', 
                   'calcular_total_receitas',
                   'criado_por', 'data_criacao']
    list_filter = ['operadora', 'ano', 'mes']
    search_fields = ['operadora', 'ano', 'mes']
    readonly_fields = ['criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao']
    
    fieldsets = (
        ('Informações Gerais', {
            'fields': ('operadora', 'ano', 'mes')
        }),
        ('Receitas de serviços a clientes retalhistas', {
            'fields': ('receitas_mensalidades',)
        }),
        ('Receitas de serviços de voz', {
            'fields': (
                'receitas_chamadas_on_net',
                'receitas_chamadas_off_net',
                'receitas_chamadas_mtn',
                'receitas_chamadas_rede_movel_b',
                'receitas_chamadas_outros',
                'receitas_servico_telefonico_fixo'
            )
        }),
        ('Receitas de chamadas internacionais', {
            'fields': (
                'receitas_chamadas_cedeao',
                'receitas_chamadas_cplp',
                'receitas_chamadas_palop',
                'receitas_chamadas_resto_africa',
                'receitas_chamadas_resto_mundo'
            )
        }),
        ('Receitas de Roaming e Mensagens', {
            'fields': (
                'receitas_voz_roaming_out',
                'receitas_mensagens',
                'receitas_mms'
            )
        }),
        ('Receitas de Dados Móveis', {
            'fields': (
                'receitas_dados_moveis',
                'receitas_internet_banda_larga',
                'receitas_videochamadas',
                'receitas_mobile_tv',
                'receitas_outros_servicos_dados'
            )
        }),
        ('Receitas de Roaming-out (excluindo voz)', {
            'fields': (
                'receitas_roaming_out_dados',
                'receitas_internet_roaming_out'
            )
        }),
        ('Outras Receitas Retalhistas', {
            'fields': ('outras_receitas_retalhistas',)
        }),
        ('Receitas de serviços a clientes grossistas', {
            'fields': (
                'receitas_terminacao_voz',
                'receitas_terminacao_dados',
                'receitas_originacao_trafego',
                'receitas_servicos_especiais',
                'outras_receitas_grossistas'
            )
        }),
        ('Metadados', {
            'fields': ('criado_por', 'data_criacao', 'atualizado_por', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.criado_por = request.user
        obj.atualizado_por = request.user
        super().save_model(request, obj, form, change)

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('ano', 'mes', 'operadora')
        return self.readonly_fields