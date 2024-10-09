from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from ..models.trafego_originado import TrafegoOriginadoIndicador
from ..forms.trafego_originado import TrafegoOriginadoForm

class TrafegoOriginadoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = TrafegoOriginadoIndicador
    form_class = TrafegoOriginadoForm
    template_name = 'questionarios/trafego_originado_form.html'
    success_url = reverse_lazy('trafego_originado_list')
    permission_required = 'questionarios.add_trafegooriginadoindicador'

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super().form_valid(form)

class TrafegoOriginadoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = TrafegoOriginadoIndicador
    template_name = 'questionarios/trafego_originado_list.html'
    context_object_name = 'trafego_originado_list'
    permission_required = 'questionarios.view_trafegooriginadoindicador'

class TrafegoOriginadoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TrafegoOriginadoIndicador
    form_class = TrafegoOriginadoForm
    template_name = 'questionarios/trafego_originado_form.html'
    success_url = reverse_lazy('trafego_originado_list')
    permission_required = 'questionarios.change_trafegooriginadoindicador'

    def form_valid(self, form):
        form.instance.atualizado_por = self.request.user
        return super().form_valid(form)

class TrafegoOriginadoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = TrafegoOriginadoIndicador
    template_name = 'questionarios/trafego_originado_confirm_delete.html'
    success_url = reverse_lazy('trafego_originado_list')
    permission_required = 'questionarios.delete_trafegooriginadoindicador'

class TrafegoOriginadoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = TrafegoOriginadoIndicador
    template_name = 'questionarios/trafego_originado_detail.html'
    context_object_name = 'indicador'
    permission_required = 'questionarios.view_trafegooriginadoindicador'