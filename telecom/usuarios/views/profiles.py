# usuarios/views/profiles.py
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, DetailView, View, TemplateView
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, 
    PasswordResetView, PasswordResetConfirmView
)
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.translation import gettext as _
from django.http import JsonResponse
from allauth.account.models import EmailConfirmation, EmailAddress
from allauth.account.utils import send_email_confirmation

from ..decorators import approved_user_required
from ..models import CustomUser
from ..forms import CustomUserChangeForm

# Profile Views
@method_decorator([login_required, approved_user_required], name='dispatch')
class ProfileDetailView(DetailView):
    model = CustomUser
    template_name = 'usuarios/profile/view_profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_permissions'] = self.request.user.permissions.filter(is_active=True)
        if self.request.user.is_operator:
            context['operator_profile'] = self.request.user.operator_profile
        return context

@method_decorator([login_required, approved_user_required], name='dispatch')
class ProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'usuarios/profile/edit_profile.html'
    success_url = reverse_lazy('profile_view')

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, _('Perfil atualizado com sucesso.'))
        return super().form_valid(form)

# Authentication Views
class CustomLoginView(LoginView):
    template_name = 'usuarios/auth/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = 'login'

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'usuarios/auth/password_change.html'
    success_url = reverse_lazy('profile_view')

    def form_valid(self, form):
        messages.success(self.request, _('Sua senha foi alterada com sucesso.'))
        return super().form_valid(form)

class CustomPasswordResetView(PasswordResetView):
    template_name = 'usuarios/auth/password_reset.html'
    email_template_name = 'usuarios/email/password_reset_email.html'
    subject_template_name = 'usuarios/email/password_reset_subject.txt'
    success_url = reverse_lazy('login')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'usuarios/auth/password_reset_confirm.html'
    success_url = reverse_lazy('login')

# Email Management Views
class ApproveEmailView(View):
    def get(self, request, key):
        try:
            email_confirmation = EmailConfirmation.objects.get(key=key)
            email_address = email_confirmation.email_address
            email_address.verified = True
            email_address.set_as_primary(conditional=True)
            email_address.save()
            
            messages.success(request, _('Seu email foi confirmado com sucesso.'))
            return redirect('login')
        except (EmailConfirmation.DoesNotExist, EmailAddress.DoesNotExist):
            messages.error(request, _('Link de confirmação inválido ou expirado.'))
            return redirect('login')

class ChangeEmailView(View):
    template_name = 'usuarios/profile/change_email.html'
    success_url = reverse_lazy('profile_view')

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def post(self, request):
        new_email = request.POST.get('email')
        user = request.user
        
        if new_email and new_email != user.email:
            if CustomUser.objects.filter(email=new_email).exists():
                messages.error(request, _('Este email já está em uso.'))
                return redirect('change_email')

            user.email = new_email
            user.save()
            EmailAddress.objects.add_email(request, user, new_email, confirm=True)
            messages.success(request, _('Um email de confirmação foi enviado para o novo endereço.'))
        else:
            messages.error(request, _('Por favor, forneça um novo email válido.'))
        
        return redirect(self.success_url)

# Account Management Views
class DeleteAccountView(View):
    template_name = 'usuarios/profile/delete_account.html'
    success_url = reverse_lazy('login')

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def post(self, request):
        if request.user.check_password(request.POST.get('password')):
            request.user.delete()
            messages.success(request, _('Sua conta foi excluída com sucesso.'))
            return redirect(self.success_url)
        messages.error(request, _('Senha incorreta.'))
        return redirect('profile_view')

# Help Center Views
class HelpCenterView(TemplateView):
    template_name = 'usuarios/help/help_center.html'

# API Views
class ValidateEmailView(View):
    def post(self, request):
        email = request.POST.get('email')
        is_taken = CustomUser.objects.filter(email=email).exists()
        return JsonResponse({'is_taken': is_taken})

class CheckUsernameView(View):
    def post(self, request):
        username = request.POST.get('username')
        is_taken = CustomUser.objects.filter(username=username).exists()
        return JsonResponse({'is_taken': is_taken})

class UpdateNotificationSettingsView(View):
    @method_decorator(login_required)
    def post(self, request):
        settings = request.POST.get('settings')
        request.user.notification_settings = settings
        request.user.save()
        return JsonResponse({'status': 'success'})

# Error Handlers
def custom_404(request, exception):
    return render(request, 'usuarios/errors/404.html', status=404)

def custom_500(request):
    return render(request, 'usuarios/errors/500.html', status=500)