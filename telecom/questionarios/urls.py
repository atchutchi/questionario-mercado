from django.urls import path
from .views import (
    estacoes_moveis, 
    trafego_originado, 
    trafego_terminado, 
    trafego_roaming_internacional, 
    lbi, 
    trafego_internet, 
    internet_fixo, 
    tarifario_voz,
    receitas,
    emprego,
    investimento
)

urlpatterns = [
    # Estações Móveis
    path('estacoes-moveis/', estacoes_moveis.EstacoesMoveisListView.as_view(), name='estacoes_moveis_list'),
    path('estacoes-moveis/criar/', estacoes_moveis.EstacoesMoveisCreateView.as_view(), name='estacoes_moveis_create'),
    path('estacoes-moveis/<int:pk>/', estacoes_moveis.EstacoesMoveisDetailView.as_view(), name='estacoes_moveis_detail'),
    path('estacoes-moveis/<int:pk>/editar/', estacoes_moveis.EstacoesMoveisUpdateView.as_view(), name='estacoes_moveis_update'),
    path('estacoes-moveis/<int:pk>/excluir/', estacoes_moveis.EstacoesMoveisDeleteView.as_view(), name='estacoes_moveis_delete'),
    path('estacoes-moveis/resumo/<int:ano>/', estacoes_moveis.EstacoesMoveisResumoView.as_view(), name='estacoes_moveis_resumo'),

    # Tráfego Originado
    path('trafego-originado/', trafego_originado.TrafegoOriginadoListView.as_view(), name='trafego_originado_list'),
    path('trafego-originado/criar/', trafego_originado.TrafegoOriginadoCreateView.as_view(), name='trafego_originado_create'),
    path('trafego-originado/<int:pk>/', trafego_originado.TrafegoOriginadoDetailView.as_view(), name='trafego_originado_detail'),
    path('trafego-originado/<int:pk>/editar/', trafego_originado.TrafegoOriginadoUpdateView.as_view(), name='trafego_originado_update'),
    path('trafego-originado/<int:pk>/excluir/', trafego_originado.TrafegoOriginadoDeleteView.as_view(), name='trafego_originado_delete'),
    path('trafego-originado/resumo/<int:ano>/', trafego_originado.TrafegoOriginadoResumoView.as_view(), name='trafego_originado_resumo'),

    # Tráfego Terminado
    path('trafego-terminado/', trafego_terminado.TrafegoTerminadoListView.as_view(), name='trafego_terminado_list'),
    path('trafego-terminado/criar/', trafego_terminado.TrafegoTerminadoCreateView.as_view(), name='trafego_terminado_create'),
    path('trafego-terminado/<int:pk>/', trafego_terminado.TrafegoTerminadoDetailView.as_view(), name='trafego_terminado_detail'),
    path('trafego-terminado/<int:pk>/editar/', trafego_terminado.TrafegoTerminadoUpdateView.as_view(), name='trafego_terminado_update'),
    path('trafego-terminado/<int:pk>/excluir/', trafego_terminado.TrafegoTerminadoDeleteView.as_view(), name='trafego_terminado_delete'),
    path('trafego-terminado/resumo/<int:ano>/', trafego_terminado.TrafegoTerminadoResumoView.as_view(), name='trafego_terminado_resumo'),

    # Tráfego de Roaming Internacional
    path('trafego-roaming-internacional/', trafego_roaming_internacional.TrafegoRoamingInternacionalListView.as_view(), name='trafego_roaming_internacional_list'),
    path('trafego-roaming-internacional/criar/', trafego_roaming_internacional.TrafegoRoamingInternacionalCreateView.as_view(), name='trafego_roaming_internacional_create'),
    path('trafego-roaming-internacional/<int:pk>/', trafego_roaming_internacional.TrafegoRoamingInternacionalDetailView.as_view(), name='trafego_roaming_internacional_detail'),
    path('trafego-roaming-internacional/<int:pk>/editar/', trafego_roaming_internacional.TrafegoRoamingInternacionalUpdateView.as_view(), name='trafego_roaming_internacional_update'),
    path('trafego-roaming-internacional/<int:pk>/excluir/', trafego_roaming_internacional.TrafegoRoamingInternacionalDeleteView.as_view(), name='trafego_roaming_internacional_delete'),

    #lbi
    path('lbi/', lbi.LBIListView.as_view(), name='lbi_list'),
    path('lbi/criar/', lbi.LBICreateView.as_view(), name='lbi_create'),
    path('lbi/<int:pk>/', lbi.LBIDetailView.as_view(), name='lbi_detail'),
    path('lbi/<int:pk>/editar/', lbi.LBIUpdateView.as_view(), name='lbi_update'),
    path('lbi/<int:pk>/excluir/', lbi.LBIDeleteView.as_view(), name='lbi_delete'),
    path('lbi/resumo/<int:ano>/', lbi.LBIResumoView.as_view(), name='lbi_resumo'),

    #Tráfego Internet
    path('trafego-internet/', trafego_internet.TrafegoInternetListView.as_view(), name='trafego_internet_list'),
    path('trafego-internet/criar/', trafego_internet.TrafegoInternetCreateView.as_view(), name='trafego_internet_create'),
    path('trafego-internet/<int:pk>/', trafego_internet.TrafegoInternetDetailView.as_view(), name='trafego_internet_detail'),
    path('trafego-internet/<int:pk>/editar/', trafego_internet.TrafegoInternetUpdateView.as_view(), name='trafego_internet_update'),
    path('trafego-internet/<int:pk>/excluir/', trafego_internet.TrafegoInternetDeleteView.as_view(), name='trafego_internet_delete'),
    path('trafego-internet/resumo/<int:ano>/', trafego_internet.TrafegoInternetResumoView.as_view(), name='trafego_internet_resumo'),

    #Internet Fixo
    path('internet-fixo/', internet_fixo.InternetFixoListView.as_view(), name='internet_fixo_list'),
    path('internet-fixo/criar/', internet_fixo.InternetFixoCreateView.as_view(), name='internet_fixo_create'),
    path('internet-fixo/<int:pk>/', internet_fixo.InternetFixoDetailView.as_view(), name='internet_fixo_detail'),
    path('internet-fixo/<int:pk>/editar/', internet_fixo.InternetFixoUpdateView.as_view(), name='internet_fixo_update'),
    path('internet-fixo/<int:pk>/excluir/', internet_fixo.InternetFixoDeleteView.as_view(), name='internet_fixo_delete'),
    path('internet-fixo/resumo/<int:ano>/', internet_fixo.InternetFixoResumoView.as_view(), name='internet_fixo_resumo'),

    # Tarifário Voz Orange
    path('tarifario-orange/', tarifario_voz.TarifarioVozOrangeListView.as_view(), name='tarifario_orange_list'),
    path('tarifario-orange/criar/', tarifario_voz.TarifarioVozOrangeCreateView.as_view(), name='tarifario_orange_create'),
    path('tarifario-orange/<int:pk>/', tarifario_voz.TarifarioVozOrangeDetailView.as_view(), name='tarifario_orange_detail'),
    path('tarifario-orange/<int:pk>/editar/', tarifario_voz.TarifarioVozOrangeUpdateView.as_view(), name='tarifario_orange_update'),
    path('tarifario-orange/<int:pk>/excluir/', tarifario_voz.TarifarioVozOrangeDeleteView.as_view(), name='tarifario_orange_delete'),
    path('tarifario-orange/resumo/<int:ano>/', tarifario_voz.TarifarioVozOrangeResumoView.as_view(), name='tarifario_orange_resumo'),

    # Tarifário Voz MTN
    path('tarifario-mtn/', tarifario_voz.TarifarioVozMTNListView.as_view(), name='tarifario_mtn_list'),
    path('tarifario-mtn/criar/', tarifario_voz.TarifarioVozMTNCreateView.as_view(), name='tarifario_mtn_create'),
    path('tarifario-mtn/<int:pk>/', tarifario_voz.TarifarioVozMTNDetailView.as_view(), name='tarifario_mtn_detail'),
    path('tarifario-mtn/<int:pk>/editar/', tarifario_voz.TarifarioVozMTNUpdateView.as_view(), name='tarifario_mtn_update'),
    path('tarifario-mtn/<int:pk>/excluir/', tarifario_voz.TarifarioVozMTNDeleteView.as_view(), name='tarifario_mtn_delete'),
    path('tarifario-mtn/resumo/<int:ano>/', tarifario_voz.TarifarioVozMTNResumoView.as_view(), name='tarifario_mtn_resumo'),

    # Receitas
    path('receitas/', receitas.ReceitasListView.as_view(), name='receitas_list'),
    path('receitas/criar/', receitas.ReceitasCreateView.as_view(), name='receitas_create'),
    path('receitas/<int:pk>/', receitas.ReceitasDetailView.as_view(), name='receitas_detail'),
    path('receitas/<int:pk>/editar/', receitas.ReceitasUpdateView.as_view(), name='receitas_update'),
    path('receitas/<int:pk>/excluir/', receitas.ReceitasDeleteView.as_view(), name='receitas_delete'),
    path('receitas/resumo/<int:ano>/', receitas.ReceitasResumoView.as_view(), name='receitas_resumo'),

    # Emprego
    path('emprego/', emprego.EmpregoListView.as_view(), name='emprego_list'),
    path('emprego/criar/', emprego.EmpregoCreateView.as_view(), name='emprego_create'),
    path('emprego/<int:pk>/', emprego.EmpregoDetailView.as_view(), name='emprego_detail'),
    path('emprego/<int:pk>/editar/', emprego.EmpregoUpdateView.as_view(), name='emprego_update'),
    path('emprego/<int:pk>/excluir/', emprego.EmpregoDeleteView.as_view(), name='emprego_delete'),
    path('emprego/resumo/<int:ano>/', emprego.EmpregoResumoView.as_view(), name='emprego_resumo'),

    # Investimento
    path('investimento/', investimento.InvestimentoListView.as_view(), name='investimento_list'),
    path('investimento/criar/', investimento.InvestimentoCreateView.as_view(), name='investimento_create'),
    path('investimento/<int:pk>/', investimento.InvestimentoDetailView.as_view(), name='investimento_detail'),
    path('investimento/<int:pk>/editar/', investimento.InvestimentoUpdateView.as_view(), name='investimento_update'),
    path('investimento/<int:pk>/excluir/', investimento.InvestimentoDeleteView.as_view(), name='investimento_delete'),
    path('investimento/resumo/<int:ano>/', investimento.InvestimentoResumoView.as_view(), name='investimento_resumo'),

]