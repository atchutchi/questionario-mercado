# questionarios/views/estacoes_moveis.py

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        indicador = self.get_object()
        context['total_utilizadores'] = indicador.total_utilizadores
        context['total_carregamentos'] = indicador.total_carregamentos
        context['total_levantamentos'] = indicador.total_levantamentos
        context['total_transferencias'] = indicador.total_transferencias
        return context