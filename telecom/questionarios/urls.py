from django.urls import path
from .views import estacoes_moveis, trafego_originado, trafego_terminado

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

    # Tráfego Terminado
    path('trafego-terminado/', trafego_terminado.TrafegoTerminadoListView.as_view(), name='trafego_terminado_list'),
    path('trafego-terminado/criar/', trafego_terminado.TrafegoTerminadoCreateView.as_view(), name='trafego_terminado_create'),
    path('trafego-terminado/<int:pk>/', trafego_terminado.TrafegoTerminadoDetailView.as_view(), name='trafego_terminado_detail'),
    path('trafego-terminado/<int:pk>/editar/', trafego_terminado.TrafegoTerminadoUpdateView.as_view(), name='trafego_terminado_update'),
    path('trafego-terminado/<int:pk>/excluir/', trafego_terminado.TrafegoTerminadoDeleteView.as_view(), name='trafego_terminado_delete'),
    path('trafego-terminado/resumo/<int:ano>/', trafego_terminado.TrafegoTerminadoResumoView.as_view(), name='trafego_terminado_resumo'),
]