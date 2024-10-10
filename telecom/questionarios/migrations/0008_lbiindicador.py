# Generated by Django 5.1.2 on 2024-10-10 11:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0007_trafegoroaminginternacionalindicador'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LBIIndicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('mes', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('satelite', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('cabo_fibra_optica', models.DecimalField(decimal_places=2, max_digits=10)),
                ('feixe_hertziano', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponivel_nominal_down', models.DecimalField(decimal_places=2, max_digits=10)),
                ('instalada_equipada_down', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contratada_down', models.DecimalField(decimal_places=2, max_digits=10)),
                ('utilizada_down', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponivel_nominal_up', models.DecimalField(decimal_places=2, max_digits=10)),
                ('instalada_equipada_up', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contratada_up', models.DecimalField(decimal_places=2, max_digits=10)),
                ('utilizada_up', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('atualizado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lbi_atualizado', to=settings.AUTH_USER_MODEL)),
                ('criado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lbi_criado', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('ano', 'mes')},
            },
        ),
    ]
