from django.urls import path
from .views import estacoes_moveis

urlpatterns = [
    path('estacoes-moveis/', estacoes_moveis.EstacoesMoveisListView.as_view(), name='estacoes_moveis_list'),
    path('estacoes-moveis/criar/', estacoes_moveis.EstacoesMoveisCreateView.as_view(), name='estacoes_moveis_create'),
    path('estacoes-moveis/<int:pk>/', estacoes_moveis.EstacoesMoveisDetailView.as_view(), name='estacoes_moveis_detail'),
    path('estacoes-moveis/<int:pk>/editar/', estacoes_moveis.EstacoesMoveisUpdateView.as_view(), name='estacoes_moveis_update'),
    path('estacoes-moveis/<int:pk>/excluir/', estacoes_moveis.EstacoesMoveisDeleteView.as_view(), name='estacoes_moveis_delete'),
]