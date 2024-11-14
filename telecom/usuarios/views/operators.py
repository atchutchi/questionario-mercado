
# usuarios/views/operators.py
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _

from ..decorators import admin_required
from ..models import CustomUser, OperatorProfile
from ..forms import OperatorProfileForm


@method_decorator([login_required, admin_required], name='dispatch')
class OperatorListView(ListView):
    """Lista todos os operadores do sistema."""
    model = CustomUser
    template_name = 'usuarios/operator_list.html'
    context_object_name = 'operators'

    def get_queryset(self):
        return CustomUser.objects.filter(is_operator=True)

@method_decorator([login_required, admin_required], name='dispatch')
class OperatorProfileCreateView(CreateView):
    """Cria novo perfil de operador."""
    model = OperatorProfile
    form_class = OperatorProfileForm
    template_name = 'usuarios/operator_form.html'
    success_url = reverse_lazy('operator_list')

    def form_valid(self, form):
        messages.success(self.request, _('Perfil de operador criado com sucesso.'))
        return super().form_valid(form)

@method_decorator([login_required, admin_required], name='dispatch')
class OperatorProfileUpdateView(UpdateView):
    """Atualiza perfil de operador existente."""
    model = OperatorProfile
    form_class = OperatorProfileForm
    template_name = 'usuarios/operator_form.html'
    success_url = reverse_lazy('operator_list')

    def form_valid(self, form):
        messages.success(self.request, _('Perfil de operador atualizado com sucesso.'))
        return super().form_valid(form)


@method_decorator([login_required, admin_required], name='dispatch')
class OperatorProfileDetailView(DetailView):
    """View para visualizar detalhes de um perfil de operador."""
    model = OperatorProfile
    template_name = 'usuarios/operator_detail.html'
    context_object_name = 'operator'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activities'] = self.get_operator_activities()  # Se você implementar tracking de atividades
        return context

    def get_operator_activities(self):
        # Implemente esta função se quiser mostrar atividades recentes do operador
        return []