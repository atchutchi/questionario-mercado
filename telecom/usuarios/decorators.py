# usuarios/decorators.py
from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.utils.translation import gettext as _

def admin_required(view_func):
    """
    Decorator para verificar se o usuário é um administrador.
    Redireciona para a página de login se não estiver autenticado ou
    levanta PermissionDenied se não for admin.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('Por favor, faça login para acessar esta página.'))
            return redirect('account_login')
        if not request.user.is_superuser:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def approved_user_required(view_func):
    """
    Decorator para verificar se o usuário está aprovado.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('Por favor, faça login para acessar esta página.'))
            return redirect('account_login')
        if not request.user.is_approved:
            messages.warning(request, _('Sua conta ainda não foi aprovada.'))
            return redirect('approval_pending')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def operator_required(view_func):
    """
    Decorator para verificar se o usuário é um operador.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, _('Por favor, faça login para acessar esta página.'))
            return redirect('account_login')
        if not request.user.is_operator:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def permission_required(permission_name):
    """
    Decorator para verificar permissões específicas.
    Uso: @permission_required('view_data')
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.error(request, _('Por favor, faça login para acessar esta página.'))
                return redirect('account_login')
            
            user_permission = request.user.permissions.filter(
                permission_name=permission_name,
                is_active=True
            ).exists()
            
            if not user_permission and not request.user.is_superuser:
                raise PermissionDenied
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator