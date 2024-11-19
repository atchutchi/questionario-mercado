# usuarios/views/approvals.py
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.translation import gettext as _

from ..decorators import admin_required
from ..models import CustomUser
from ..forms import UserApprovalForm

@method_decorator([login_required, admin_required], name='dispatch')
class PendingApprovalListView(ListView):
    """Lista todos os usuários pendentes de aprovação."""
    model = CustomUser
    template_name = 'usuarios/approval_list.html'
    context_object_name = 'pending_users'

    def get_queryset(self):
        return CustomUser.objects.filter(
            is_approved=False,
            is_superuser=False
        ).order_by('-date_joined')

@method_decorator([login_required, admin_required], name='dispatch')
class UserApprovalView(UpdateView):
    """View para aprovar ou rejeitar usuários."""
    model = CustomUser
    form_class = UserApprovalForm
    template_name = 'usuarios/approval_form.html'
    success_url = reverse_lazy('pending_approval_list')

    def form_valid(self, form):
        user = self.object
        if form.cleaned_data['approve']:
            user.is_approved = True
            user.approval_date = timezone.now()
            user.approved_by = self.request.user
            user.notes = form.cleaned_data['notes']
            user.save()
            messages.success(
                self.request,
                _(f'Usuário {user.email} aprovado com sucesso.')
            )
        else:
            user.delete()
            messages.warning(
                self.request,
                _(f'Usuário {user.email} rejeitado e removido do sistema.')
            )
        return redirect(self.success_url)
