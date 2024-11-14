# usuarios/views/permissions.py
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _

from ..decorators import admin_required
from ..models import CustomUser, UserPermission
from ..forms import UserPermissionForm

@method_decorator([login_required, admin_required], name='dispatch')
class PermissionListView(ListView):
    """Lista todas as permissões de usuários."""
    model = UserPermission
    template_name = 'usuarios/permission_list.html'
    context_object_name = 'permissions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = CustomUser.objects.all()
        return context

@method_decorator([login_required, admin_required], name='dispatch')
class PermissionCreateView(CreateView):
    """Cria nova permissão para um usuário."""
    model = UserPermission
    form_class = UserPermissionForm
    template_name = 'usuarios/permission_form.html'
    success_url = reverse_lazy('permission_list')

    def form_valid(self, form):
        form.instance.granted_by = self.request.user
        user_id = self.kwargs.get('user_id')
        form.instance.user = get_object_or_404(CustomUser, id=user_id)
        
        messages.success(
            self.request,
            _('Permissão concedida com sucesso.')
        )
        return super().form_valid(form)

@method_decorator([login_required, admin_required], name='dispatch')
class PermissionUpdateView(UpdateView):
    """Atualiza uma permissão existente."""
    model = UserPermission
    form_class = UserPermissionForm
    template_name = 'usuarios/permission_form.html'
    success_url = reverse_lazy('permission_list')

    def form_valid(self, form):
        messages.success(
            self.request,
            _('Permissão atualizada com sucesso.')
        )
        return super().form_valid(form)

@method_decorator([login_required, admin_required], name='dispatch')
class PermissionDeleteView(DeleteView):
    """Remove uma permissão."""
    model = UserPermission
    template_name = 'usuarios/permission_confirm_delete.html'
    success_url = reverse_lazy('permission_list')

    def delete(self, request, *args, **kwargs):
        messages.warning(
            request,
            _('Permissão removida com sucesso.')
        )
        return super().delete(request, *args, **kwargs)