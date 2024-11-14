# usuarios/views/dashboard.py
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

from ..decorators import approved_user_required
from ..models import CustomUser, OperatorProfile

@method_decorator([login_required, approved_user_required], name='dispatch')
class AdminDashboardView(TemplateView):
    """Dashboard para administradores."""
    template_name = 'usuarios/admin_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Estatísticas gerais
        context['total_users'] = CustomUser.objects.count()
        context['pending_approvals'] = CustomUser.objects.filter(
            is_approved=False
        ).count()
        context['total_operators'] = CustomUser.objects.filter(
            is_operator=True
        ).count()

        # Usuários recentes
        context['recent_users'] = CustomUser.objects.order_by(
            '-date_joined'
        )[:5]

        # Operadores com licença próxima do vencimento
        thirty_days_from_now = timezone.now().date() + timedelta(days=30)
        context['expiring_licenses'] = OperatorProfile.objects.filter(
            license_expiry__lte=thirty_days_from_now,
            license_expiry__gte=timezone.now().date()
        )

        return context

@method_decorator([login_required, approved_user_required], name='dispatch')
class UserDashboardView(TemplateView):
    """Dashboard para usuários regulares."""
    template_name = 'usuarios/user_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Informações do usuário
        context['user_info'] = {
            'last_login': user.last_login,
            'member_since': user.date_joined,
            'permissions': user.permissions.filter(is_active=True)
        }

        # Se for operador, adiciona informações específicas
        if user.is_operator:
            operator_profile = user.operator_profile
            context['operator_info'] = {
                'license_status': operator_profile.is_license_valid(),
                'license_expiry': operator_profile.license_expiry,
                'service_areas': operator_profile.get_service_areas_display()
            }

        return context