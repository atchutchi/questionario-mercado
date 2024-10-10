from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from ..models.estacoes_moveis import EstacoesMoveisIndicador
from ..forms.estacoes_moveis import EstacoesMoveisForm

class EstacoesMoveisCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = EstacoesMoveisIndicador
    form_class = EstacoesMoveisForm
    template_name = 'questionarios/estacoes_moveis_form.html'
    success_url = reverse_lazy('estacoes_moveis_list')
    permission_required = 'questionarios.add_estacoesmoveisindicador'

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super().form_valid(form)

class EstacoesMoveisListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = EstacoesMoveisIndicador
    template_name = 'questionarios/estacoes_moveis_list.html'
    context_object_name = 'estacoes_moveis_list'
    permission_required = 'questionarios.view_estacoesmoveisindicador'

class EstacoesMoveisUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = EstacoesMoveisIndicador
    form_class = EstacoesMoveisForm
    template_name = 'questionarios/estacoes_moveis_form.html'
    success_url = reverse_lazy('estacoes_moveis_list')
    permission_required = 'questionarios.change_estacoesmoveisindicador'

    def form_valid(self, form):
        form.instance.atualizado_por = self.request.user
        return super().form_valid(form)

class EstacoesMoveisDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = EstacoesMoveisIndicador
    template_name = 'questionarios/estacoes_moveis_confirm_delete.html'
    success_url = reverse_lazy('estacoes_moveis_list')
    permission_required = 'questionarios.delete_estacoesmoveisindicador'

class EstacoesMoveisDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = EstacoesMoveisIndicador
    template_name = 'questionarios/estacoes_moveis_detail.html'
    context_object_name = 'indicador'
    permission_required = 'questionarios.view_estacoesmoveisindicador'

class EstacoesMoveisResumoView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = EstacoesMoveisIndicador
    template_name = 'questionarios/estacoes_moveis_resumo.html'
    context_object_name = 'indicadores'
    permission_required = 'questionarios.view_estacoesmoveisindicador'

    def get_queryset(self):
        ano = self.kwargs.get('ano')
        return EstacoesMoveisIndicador.objects.filter(ano=ano).order_by('mes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ano = self.kwargs.get('ano')
        indicadores = self.get_queryset()

        # Cálculos trimestrais
        totais_trimestrais = []
        for trimestre in range(1, 5):
            meses = range((trimestre - 1) * 3 + 1, trimestre * 3 + 1)
            dados_trimestre = indicadores.filter(mes__in=meses)
            
            total_utilizadores = sum(dado.calcular_total_utilizadores() for dado in dados_trimestre)
            total_carregamentos = sum(dado.calcular_total_carregamentos() for dado in dados_trimestre)
            total_levantamentos = sum(dado.calcular_total_levantamentos() for dado in dados_trimestre)
            total_transferencias = sum(dado.calcular_total_transferencias() for dado in dados_trimestre)
            total_estacoes_moveis = sum(dado.calcular_total_estacoes_moveis() for dado in dados_trimestre)
            
            totais_trimestrais.append({
                'trimestre': trimestre,
                'total_utilizadores': total_utilizadores,
                'total_carregamentos': total_carregamentos,
                'total_levantamentos': total_levantamentos,
                'total_transferencias': total_transferencias,
                'total_estacoes_moveis': total_estacoes_moveis
            })

        # Cálculos anuais
        total_utilizadores_anual = sum(dado.calcular_total_utilizadores() for dado in indicadores)
        total_carregamentos_anual = sum(dado.calcular_total_carregamentos() for dado in indicadores)
        total_levantamentos_anual = sum(dado.calcular_total_levantamentos() for dado in indicadores)
        total_transferencias_anual = sum(dado.calcular_total_transferencias() for dado in indicadores)
        total_estacoes_moveis_anual = sum(dado.calcular_total_estacoes_moveis() for dado in indicadores)

        context['ano'] = ano
        context['totais_trimestrais'] = totais_trimestrais
        context['total_utilizadores_anual'] = total_utilizadores_anual
        context['total_carregamentos_anual'] = total_carregamentos_anual
        context['total_levantamentos_anual'] = total_levantamentos_anual
        context['total_transferencias_anual'] = total_transferencias_anual
        context['total_estacoes_moveis_anual'] = total_estacoes_moveis_anual

        return context