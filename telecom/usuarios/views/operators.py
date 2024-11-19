# usuarios/views/operators.py
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _

from ..decorators import admin_required
from ..models import OperatorProfile
from ..forms import OperatorProfileForm

@method_decorator([login_required, admin_required], name='dispatch')
class OperatorListView(ListView):
    model = OperatorProfile
    template_name = 'usuarios/operator_list.html'
    context_object_name = 'operators'
    
    def get_queryset(self):
        return OperatorProfile.objects.select_related('user').all()

@method_decorator([login_required, admin_required], name='dispatch')
class OperatorProfileCreateView(CreateView):
    model = OperatorProfile
    form_class = OperatorProfileForm
    template_name = 'usuarios/operator_form.html'
    success_url = reverse_lazy('usuarios:operator-list')

    def form_valid(self, form):
        messages.success(self.request, _('Operador criado com sucesso.'))
        return super().form_valid(form)

@method_decorator([login_required, admin_required], name='dispatch')
class OperatorProfileUpdateView(UpdateView):
    model = OperatorProfile
    form_class = OperatorProfileForm
    template_name = 'usuarios/operator_form.html'
    success_url = reverse_lazy('usuarios:operator-list')

    def form_valid(self, form):
        messages.success(self.request, _('Operador atualizado com sucesso.'))
        return super().form_valid(form)

@method_decorator([login_required, admin_required], name='dispatch')
class OperatorProfileDetailView(DetailView):
    model = OperatorProfile
    template_name = 'usuarios/operator_detail.html'
    context_object_name = 'operator'