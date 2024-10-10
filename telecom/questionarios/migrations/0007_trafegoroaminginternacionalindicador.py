# Generated by Django 5.1.2 on 2024-10-10 11:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0006_trafegoterminadoindicador'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TrafegoRoamingInternacionalIndicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('mes', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('chamadas_originadas_rede', models.IntegerField()),
                ('chamadas_terminadas_rede', models.IntegerField()),
                ('minutos_originados_rede', models.IntegerField()),
                ('minutos_terminados_rede', models.IntegerField()),
                ('mensagens_escritas_enviadas', models.IntegerField()),
                ('mensagens_escritas_recebidas', models.IntegerField()),
                ('sessoes_acesso_internet', models.IntegerField()),
                ('volume_acesso_internet', models.BigIntegerField(help_text='Em Mbit')),
                ('chamadas_originadas_operador_roaming', models.IntegerField()),
                ('chamadas_terminadas_operador_roaming', models.IntegerField()),
                ('minutos_originados_operador_roaming', models.IntegerField()),
                ('minutos_terminados_operador_roaming', models.IntegerField()),
                ('mensagens_escritas_enviadas_out', models.IntegerField()),
                ('sessoes_acesso_internet_out', models.IntegerField()),
                ('volume_acesso_internet_out', models.BigIntegerField(help_text='Em Mbit')),
                ('acordos_roaming_internacional', models.IntegerField(help_text='Número de países')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('atualizado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trafego_roaming_internacional_atualizado', to=settings.AUTH_USER_MODEL)),
                ('criado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trafego_roaming_internacional_criado', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('ano', 'mes')},
            },
        ),
    ]
