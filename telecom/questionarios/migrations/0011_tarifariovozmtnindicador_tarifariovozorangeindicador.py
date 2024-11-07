# Generated by Django 5.1.2 on 2024-10-29 14:08

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0010_internetfixoindicador'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TarifarioVozMTNIndicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('mes', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('operadora', models.CharField(default='MTN', editable=False, max_length=50)),
                ('huawei_4g_lte', models.IntegerField(help_text='Huawei 4G LTE - 30,000F', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Huawei 4G LTE')),
                ('huawei_mobile_wifi_4g', models.IntegerField(help_text='Huawei Mobile Wi-Fi 4G - 20,000F', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Huawei Mobile Wi-Fi 4G')),
                ('pacote_30mb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='100F - 30MB')),
                ('pacote_100mb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='200F - 100MB')),
                ('pacote_300mb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='400F - 300MB')),
                ('pacote_1gb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='500F - 1GB')),
                ('pacote_650mb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='1000F - 650MB')),
                ('pacote_1000mb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='2000F - 1000MB')),
                ('pacote_1_5gb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='4000 - 1,5GB')),
                ('pacote_10gb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='10,000 - 10GB')),
                ('pacote_18gb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='15,000 - 18GB')),
                ('pacote_30gb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='21,000 - 30GB')),
                ('pacote_50gb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='25,000 - 50GB')),
                ('pacote_60gb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='30,000 - 60GB')),
                ('pacote_120gb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='50,000 - 120GB')),
                ('pacote_yello_350mb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='200F - 350MB')),
                ('pacote_yello_1_5gb', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='500F - 1.5GB')),
                ('pacote_yello_1_5gb_7dias', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='800F - 1.5GB/7dias')),
                ('pacote_1hora', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='200F - 1 hora ilimitado')),
                ('pacote_3horas', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='400F - 3 horas ilimitado')),
                ('pacote_9horas', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='1000F - 9 horas ilimitado')),
                ('taxa_imposto', models.CharField(default='19%', max_length=50, verbose_name='Taxa/Imposto incluído')),
                ('link_plano', models.URLField(blank=True, null=True, verbose_name='Link onde o plano tarifário é publicado')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('atualizado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tarifario_mtn_atualizado', to=settings.AUTH_USER_MODEL)),
                ('criado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tarifario_mtn_criado', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tarifário MTN',
                'verbose_name_plural': 'Tarifários MTN',
                'unique_together': {('ano', 'mes')},
            },
        ),
        migrations.CreateModel(
            name='TarifarioVozOrangeIndicador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('mes', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)])),
                ('dongle_3g', models.IntegerField(verbose_name='Dongle 3G')),
                ('dongle_4g', models.IntegerField(verbose_name='Dongle 4G')),
                ('airbox_4g', models.IntegerField(verbose_name='Airbox 4G')),
                ('flybox_4g', models.IntegerField(verbose_name='Flybox 4G')),
                ('flybox_4g_plus', models.IntegerField(verbose_name='Flybox 4G+')),
                ('casa_zen_2mbits_adesao', models.IntegerField(verbose_name='Orange Internet Casa Zen 2 Mbit/s - Adesão')),
                ('casa_conforto_4mbits_adesao', models.IntegerField(verbose_name='Orange Internet Casa Conforto 4 Mbit/s - Adesão')),
                ('casabox_2mbits_adesao', models.IntegerField(verbose_name='Casabox 2 Mbit/s - Adesão')),
                ('casabox_5mbits_adesao', models.IntegerField(verbose_name='Casabox 5 Mbit/s - Adesão')),
                ('casa_zen_2mbits_mensal', models.IntegerField(verbose_name='Orange Internet Casa Zen 2 Mbit/s - Mensal')),
                ('casa_conforto_4mbits_mensal', models.IntegerField(verbose_name='Orange Internet Casa Conforto 4 Mbit/s - Mensal')),
                ('casabox_2mbits_mensal', models.IntegerField(verbose_name='Casabox 2 Mbit/s - Mensal')),
                ('casabox_5mbits_mensal', models.IntegerField(verbose_name='Casabox 5 Mbit/s - Mensal')),
                ('pass_ilimite_1h', models.IntegerField(verbose_name='Pass Ilimité 1h')),
                ('pass_ilimite_3h', models.IntegerField(verbose_name='Pass Ilimité 3h')),
                ('pass_ilimite_8h', models.IntegerField(verbose_name='Pass Ilimité 8h')),
                ('pass_ilimite_dimanche', models.IntegerField(verbose_name='Pass Ilimité Dimanche')),
                ('pass_ilimite_nuit', models.IntegerField(verbose_name='Pass Ilimité Nuit')),
                ('pass_jours_ferie', models.IntegerField(verbose_name='Pass Jours Férié')),
                ('pass_30_mo', models.IntegerField(verbose_name='Pass 30 Mo')),
                ('pass_75_mo', models.IntegerField(verbose_name='Pass 75 Mo')),
                ('pass_150_mo', models.IntegerField(verbose_name='Pass 150 Mo')),
                ('pass_250_mo', models.IntegerField(verbose_name='Pass 250 Mo')),
                ('pass_500_mo', models.IntegerField(verbose_name='Pass 500 Mo')),
                ('pass_600_mo', models.IntegerField(verbose_name='Pass 600 Mo')),
                ('pass_1_5_go', models.IntegerField(verbose_name='Pass 1.5 Go')),
                ('pass_3_go', models.IntegerField(verbose_name='Pass 3 Go')),
                ('pass_10_go', models.IntegerField(verbose_name='Pass 10 Go')),
                ('pass_18_go', models.IntegerField(verbose_name='Pass 18 Go')),
                ('pass_35_go', models.IntegerField(verbose_name='Pass 35 Go')),
                ('pass_100_go', models.IntegerField(verbose_name='Pass 100 Go')),
                ('pass_400_mo', models.IntegerField(verbose_name='Pass 400 Mo')),
                ('pass_1_go', models.IntegerField(verbose_name='Pass 1 Go')),
                ('cartao_sim_adesao', models.IntegerField(verbose_name='Assinatura/Adesão ao serviço/cartão SIM')),
                ('taxa_adesao', models.CharField(max_length=50, verbose_name='Taxa/Imposto incluído')),
                ('tarifa_orange_livre_6h_22h', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Orange Livre - 06h-22h')),
                ('tarifa_orange_livre_22h_6h', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Orange Livre - 22h-06h')),
                ('tarifa_orange_jovem_vip_jovem', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Orange Jovem VIP - entre Jovem VIP')),
                ('tarifa_orange_jovem_vip_6h_22h', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Orange Jovem VIP - 06h-22h')),
                ('tarifa_orange_jovem_vip_22h_6h', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Orange Jovem VIP - 22h-06h')),
                ('tarifa_orange_intenso', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Orange Intenso')),
                ('tarifa_offnet_orange_livre', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Orange Livre')),
                ('tarifa_offnet_orange_jovem_vip', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Orange Jovem VIP')),
                ('tarifa_offnet_orange_intenso', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Orange Intenso')),
                ('tarifa_zona1', models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Zone 1: Côte d'Ivoire, Mali")),
                ('tarifa_zona2', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Zone 2: Cape Vert, Angola, Brasil...')),
                ('tarifa_zona3', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Zone 3: Royaume Uni, Espagne...')),
                ('tarifa_zona4', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Zone 4: Niger, Mauritanie, Reste du monde')),
                ('tarifa_zona5', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Zone 5: Guinée Conakry')),
                ('tarifa_zona6', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Zone 6: Gambie')),
                ('toll_free', models.IntegerField(blank=True, null=True, verbose_name='Toll Free')),
                ('vpn', models.IntegerField(blank=True, null=True, verbose_name='VPN')),
                ('taxa_imposto', models.CharField(max_length=50, verbose_name='Taxa/Imposto incluído')),
                ('promocoes', models.TextField(blank=True, null=True, verbose_name='Promoções')),
                ('link_plano', models.URLField(blank=True, null=True, verbose_name='Link onde o plano tarifário é publicado')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('atualizado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tarifario_orange_atualizado', to=settings.AUTH_USER_MODEL)),
                ('criado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tarifario_orange_criado', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tarifário Orange',
                'verbose_name_plural': 'Tarifários Orange',
                'unique_together': {('ano', 'mes')},
            },
        ),
    ]