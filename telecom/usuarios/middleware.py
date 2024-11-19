# usuarios/middleware.py
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.utils.translation import gettext as _
from django.conf import settings

class ApprovalMiddleware:
    """
    Middleware para verificar se o usuário está aprovado.
    Redireciona usuários não aprovados para uma página de espera.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # URLs que podem ser acessadas mesmo sem aprovação
        self.public_urls = [
            '/accounts/logout/',
            '/accounts/password/reset/',
            '/usuarios/approval-pending/',
            '/static/',
            '/media/',
            '/admin/',
            '/usuarios/login/',
            '/usuarios/logout/',
        ]

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_superuser:
            # Verifica se o caminho atual não está na lista de URLs públicas
            if not any(request.path.startswith(url) for url in self.public_urls):
                if not request.user.is_approved:
                    messages.warning(
                        request,
                        _('Sua conta ainda está pendente de aprovação.')
                    )
                    return redirect('usuarios:approval_pending')

        response = self.get_response(request)
        return response