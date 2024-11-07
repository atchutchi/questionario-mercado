# Generated by Django 5.1.2 on 2024-11-07 15:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0013_alter_internetfixoindicador_unique_together_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceitasIndicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('mes', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('operadora', models.CharField(blank=True, choices=[('orange', 'Orange'), ('mtn', 'MTN')], max_length=10, null=True, verbose_name='Operadora')),
                ('receitas_mensalidades', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Receitas de Mensalidades')),
                ('receitas_chamadas_on_net', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Receitas de chamadas On-net')),
                ('receitas_chamadas_off_net', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Receitas de chamadas para outros STM nacionais')),
                ('receitas_chamadas_mtn', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Para o operador da rede móvel MTN')),
                ('receitas_chamadas_rede_movel_b', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Para o operador da rede móvel B')),
                ('receitas_chamadas_outros', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Outros')),
                ('receitas_servico_telefonico_fixo', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Receitas de chamadas para serviço telefónico fixo')),
                ('receitas_chamadas_cedeao', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='CEDEAO')),
                ('receitas_chamadas_cplp', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='CPLP')),
                ('receitas_chamadas_palop', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='PALOP')),
                ('receitas_chamadas_resto_africa', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Resto de África')),
                ('receitas_chamadas_resto_mundo', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Resto do mundo')),
                ('receitas_voz_roaming_out', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Receitas de serviços de voz em Roaming-out')),
                ('receitas_mensagens', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Receitas de serviços de mensagens')),
                ('receitas_mms', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Receitas de MMS')),
                ('receitas_dados_moveis', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Receitas de serviços de dados móveis')),
                ('receitas_internet_banda_larga', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Receitas de acesso à Internet em banda larga')),
                ('receitas_videochamadas', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Receitas de videochamadas')),
                ('receitas_mobile_tv', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Receitas de Mobile TV')),
                ('receitas_outros_servicos_dados', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Receitas de outros serviços de dados')),
                ('receitas_roaming_out_dados', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Receitas de Roaming-out excluindo comunicações de voz')),
                ('receitas_internet_roaming_out', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Receitas de acesso à Internet em banda larga em roaming-out')),
                ('outras_receitas_retalhistas', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Outras receitas retalhistas')),
                ('receitas_terminacao_voz', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Receitas de terminação de voz')),
                ('receitas_terminacao_dados', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Receitas de terminação de dados')),
                ('receitas_originacao_trafego', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Receitas de originação de tráfego para serviços especiais')),
                ('receitas_servicos_especiais', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Receitas do serviço de facturação e cobrança pela originação de chamadas para serviços especiais')),
                ('outras_receitas_grossistas', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Outras receitas grossistas')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('atualizado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receitas_atualizado', to=settings.AUTH_USER_MODEL)),
                ('criado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receitas_criado', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Receitas',
                'verbose_name_plural': 'Receitas',
                'unique_together': {('ano', 'mes', 'operadora')},
            },
        ),
    ]