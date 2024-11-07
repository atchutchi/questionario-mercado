from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from ..models.trafego_internet import TrafegoInternetIndicador
from ..forms.trafego_internet import TrafegoInternetForm

class TrafegoInternetCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = TrafegoInternetIndicador
    form_class = TrafegoInternetForm
    template_name = 'questionarios/trafego_internet_form.html'
    success_url = reverse_lazy('trafego_internet_list')
    permission_required = 'questionarios.add_trafegointernettindicador'

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super().form_valid(form)

class TrafegoInternetListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = TrafegoInternetIndicador
    template_name = 'questionarios/trafego_internet_list.html'
    context_object_name = 'trafego_internet_list'
    permission_required = 'questionarios.view_trafegointernettindicador'

    def get_queryset(self):
        queryset = super().get_queryset()
        operadora = self.request.GET.get('operadora')
        if operadora:
            queryset = queryset.filter(operadora=operadora)
        return queryset.order_by('-ano', '-mes')

class TrafegoInternetUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TrafegoInternetIndicador
    form_class = TrafegoInternetForm
    template_name = 'questionarios/trafego_internet_form.html'
    success_url = reverse_lazy('trafego_internet_list')
    permission_required = 'questionarios.change_trafegointernettindicador'

    def form_valid(self, form):
        form.instance.atualizado_por = self.request.user
        return super().form_valid(form)

class TrafegoInternetDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = TrafegoInternetIndicador
    template_name = 'questionarios/trafego_internet_confirm_delete.html'
    success_url = reverse_lazy('trafego_internet_list')
    permission_required = 'questionarios.delete_trafegointernettindicador'

class TrafegoInternetDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = TrafegoInternetIndicador
    template_name = 'questionarios/trafego_internet_detail.html'
    context_object_name = 'indicador'
    permission_required = 'questionarios.view_trafegointernettindicador'

class TrafegoInternetResumoView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = TrafegoInternetIndicador
    template_name = 'questionarios/trafego_internet_resumo.html'
    context_object_name = 'indicadores'
    permission_required = 'questionarios.view_trafegointernettindicador'

    def get_queryset(self):
        ano = self.kwargs.get('ano')
        operadora = self.request.GET.get('operadora')
        queryset = self.model.objects.filter(ano=ano)
        if operadora:
            queryset = queryset.filter(operadora=operadora)
        return queryset.order_by('mes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operadora_selecionada'] = self.request.GET.get('operadora')
        ano = self.kwargs.get('ano')
        indicadores = self.get_queryset()

        # Cálculos trimestrais
        totais_trimestrais = []
        for trimestre in range(1, 5):
            meses = range((trimestre - 1) * 3 + 1, trimestre * 3 + 1)
            dados_trimestre = indicadores.filter(mes__in=meses)
            
            total_trafego = sum(dado.calcular_total_trafego() for dado in dados_trimestre)
            total_banda_larga = sum(dado.calcular_total_banda_larga() for dado in dados_trimestre)
            total_categoria = sum(dado.calcular_total_categoria() for dado in dados_trimestre)
            total_regiao = sum(dado.calcular_total_regiao() for dado in dados_trimestre)
            
            totais_trimestrais.append({
                'trimestre': trimestre,
                'total_trafego': total_trafego,
                'total_banda_larga': total_banda_larga,
                'total_categoria': total_categoria,
                'total_regiao': total_regiao,
            })

        # Cálculos anuais
        total_trafego_anual = sum(dado.calcular_total_trafego() for dado in indicadores)
        total_banda_larga_anual = sum(dado.calcular_total_banda_larga() for dado in indicadores)
        total_categoria_anual = sum(dado.calcular_total_categoria() for dado in indicadores)
        total_regiao_anual = sum(dado.calcular_total_regiao() for dado in indicadores)

        context['ano'] = ano
        context['totais_trimestrais'] = totais_trimestrais
        context['total_trafego_anual'] = total_trafego_anual
        context['total_banda_larga_anual'] = total_banda_larga_anual
        context['total_categoria_anual'] = total_categoria_anual
        context['total_regiao_anual'] = total_regiao_anual

        return context