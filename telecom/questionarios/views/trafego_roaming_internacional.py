from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from ..models.trafego_roaming_internacional import TrafegoRoamingInternacionalIndicador
from ..forms.trafego_roaming_internacional import TrafegoRoamingInternacionalForm

class TrafegoRoamingInternacionalCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = TrafegoRoamingInternacionalIndicador
    form_class = TrafegoRoamingInternacionalForm
    template_name = 'questionarios/trafego_roaming_internacional_form.html'
    success_url = reverse_lazy('trafego_roaming_internacional_list')
    permission_required = 'questionarios.add_trafegoroaminginternacionalindicador'

    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        return super().form_valid(form)

class TrafegoRoamingInternacionalListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = TrafegoRoamingInternacionalIndicador
    template_name = 'questionarios/trafego_roaming_internacional_list.html'
    context_object_name = 'trafego_roaming_internacional_list'
    permission_required = 'questionarios.view_trafegoroaminginternacionalindicador'

class TrafegoRoamingInternacionalUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = TrafegoRoamingInternacionalIndicador
    form_class = TrafegoRoamingInternacionalForm
    template_name = 'questionarios/trafego_roaming_internacional_form.html'
    success_url = reverse_lazy('trafego_roaming_internacional_list')
    permission_required = 'questionarios.change_trafegoroaminginternacionalindicador'

    def form_valid(self, form):
        form.instance.atualizado_por = self.request.user
        return super().form_valid(form)

class TrafegoRoamingInternacionalDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = TrafegoRoamingInternacionalIndicador
    template_name = 'questionarios/trafego_roaming_internacional_confirm_delete.html'
    success_url = reverse_lazy('trafego_roaming_internacional_list')
    permission_required = 'questionarios.delete_trafegoroaminginternacionalindicador'

class TrafegoRoamingInternacionalDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = TrafegoRoamingInternacionalIndicador
    template_name = 'questionarios/trafego_roaming_internacional_detail.html'
    context_object_name = 'indicador'
    permission_required = 'questionarios.view_trafegoroaminginternacionalindicador'