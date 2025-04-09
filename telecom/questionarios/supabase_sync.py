"""
Módulo para sincronização de dados com o Supabase
"""
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from telecom.supabase import get_supabase_client

from .models import (
    EstacoesMoveisIndicador,
    TrafegoOriginadoIndicador,
    TrafegoTerminadoIndicador,
    TrafegoRoamingInternacionalIndicador,
    LBIIndicador,
    TrafegoInternetIndicador,
    InternetFixoIndicador,
    ReceitasIndicador,
    EmpregoIndicador,
    InvestimentoIndicador
)

# Mapeamento de modelos para tabelas no Supabase
MODEL_TABLE_MAP = {
    EstacoesMoveisIndicador: 'estacoes_moveis',
    TrafegoOriginadoIndicador: 'trafego_originado',
    TrafegoTerminadoIndicador: 'trafego_terminado',
    TrafegoRoamingInternacionalIndicador: 'trafego_roaming',
    LBIIndicador: 'lbi',
    TrafegoInternetIndicador: 'trafego_internet',
    InternetFixoIndicador: 'internet_fixo',
    ReceitasIndicador: 'receitas',
    EmpregoIndicador: 'emprego',
    InvestimentoIndicador: 'investimento',
}

def serialize_model(instance):
    """
    Serializa um modelo para envio ao Supabase
    """
    data = {}
    for field in instance._meta.fields:
        if field.name != 'id':
            value = getattr(instance, field.name)
            # Tratar campos relacionados (ForeignKey)
            if hasattr(value, 'id'):
                value = value.id
            data[field.name] = value
    
    # Adicionar o ID do Django como referência
    data['django_id'] = instance.id
    return data

@receiver(post_save)
def sync_to_supabase(sender, instance, **kwargs):
    """
    Sincroniza um modelo do Django com o Supabase após salvar
    """
    if sender in MODEL_TABLE_MAP:
        table_name = MODEL_TABLE_MAP[sender]
        data = serialize_model(instance)
        
        supabase = get_supabase_client()
        supabase.table(table_name).upsert(data).execute()

@receiver(post_delete)
def delete_from_supabase(sender, instance, **kwargs):
    """
    Remove um modelo do Supabase após excluir do Django
    """
    if sender in MODEL_TABLE_MAP and hasattr(instance, 'id'):
        table_name = MODEL_TABLE_MAP[sender]
        
        supabase = get_supabase_client()
        supabase.table(table_name).delete().eq('django_id', instance.id).execute()

def sync_all_data():
    """
    Sincroniza todos os dados existentes com o Supabase
    Útil para migração inicial
    """
    for model, table in MODEL_TABLE_MAP.items():
        instances = model.objects.all()
        
        supabase = get_supabase_client()
        for instance in instances:
            data = serialize_model(instance)
            supabase.table(table).upsert(data).execute() 