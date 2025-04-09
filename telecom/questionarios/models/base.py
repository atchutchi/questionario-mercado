from django.db import models
from telecom.supabase import get_supabase_client

class IndicadorBase(models.Model):
    OPERADORA_CHOICES = [
        ('orange', 'Orange'),
        ('mtn', 'MTN'),
        ('telecel', 'TELECEL'),
    ]
    
    ano = models.IntegerField()
    mes = models.IntegerField(choices=[(i, i) for i in range(1, 13)])
    operadora = models.CharField(
        max_length=10,
        choices=OPERADORA_CHOICES,
        verbose_name="Operadora",
        null=True,  # Permite valores nulos temporariamente
        blank=True  # Permite valores em branco temporariamente
    )

    class Meta:
        abstract = True
        
    def save_to_supabase(self, table_name):
        """
        Salva os dados do modelo no Supabase
        """
        supabase = get_supabase_client()
        data = {field.name: getattr(self, field.name) for field in self._meta.fields if field.name != 'id'}
        data['django_id'] = self.id
        
        supabase.table(table_name).upsert(data).execute()
        
    def delete_from_supabase(self, table_name):
        """
        Remove os dados do modelo no Supabase
        """
        supabase = get_supabase_client()
        supabase.table(table_name).delete().eq('django_id', self.id).execute()