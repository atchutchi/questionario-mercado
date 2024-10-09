from django.urls import path
from .views import estacoes_moveis,trafego_originado

urlpatterns = [
    path('estacoes-moveis/', estacoes_moveis.EstacoesMoveisListView.as_view(), name='estacoes_moveis_list'),
    path('estacoes-moveis/criar/', estacoes_moveis.EstacoesMoveisCreateView.as_view(), name='estacoes_moveis_create'),
    path('estacoes-moveis/<int:pk>/', estacoes_moveis.EstacoesMoveisDetailView.as_view(), name='estacoes_moveis_detail'),
    path('estacoes-moveis/<int:pk>/editar/', estacoes_moveis.EstacoesMoveisUpdateView.as_view(), name='estacoes_moveis_update'),
    path('estacoes-moveis/<int:pk>/excluir/', estacoes_moveis.EstacoesMoveisDeleteView.as_view(), name='estacoes_moveis_delete'),
    path('trafego-originado/', trafego_originado.TrafegoOriginadoListView.as_view(), name='trafego_originado_list'),
    path('trafego-originado/criar/', trafego_originado.TrafegoOriginadoCreateView.as_view(), name='trafego_originado_create'),
    path('trafego-originado/<int:pk>/', trafego_originado.TrafegoOriginadoDetailView.as_view(), name='trafego_originado_detail'),
    path('trafego-originado/<int:pk>/editar/', trafego_originado.TrafegoOriginadoUpdateView.as_view(), name='trafego_originado_update'),
    path('trafego-originado/<int:pk>/excluir/', trafego_originado.TrafegoOriginadoDeleteView.as_view(), name='trafego_originado_delete'),

]