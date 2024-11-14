# usuarios/signals.py
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, OperatorProfile

@receiver(post_save, sender=CustomUser)
def create_operator_profile(sender, instance, created, **kwargs):
    """
    Cria automaticamente um perfil de operador quando um usuário
    é criado com is_operator=True
    """
    if created and instance.is_operator:
        OperatorProfile.objects.create(
            user=instance,
            operator_name=f"{instance.first_name} {instance.last_name}".strip()
        )

@receiver(post_save, sender=CustomUser)
def send_approval_notification(sender, instance, created, **kwargs):
    """
    Envia notificações por email quando um usuário é criado ou aprovado
    """
    if created:
        # Notifica administradores sobre novo registro
        admins = CustomUser.objects.filter(is_superuser=True)
        context = {'user': instance}
        
        html_message = render_to_string(
            'usuarios/email/new_user_notification.html',
            context
        )
        
        for admin in admins:
            send_mail(
                subject=_('Novo usuário aguardando aprovação'),
                message=_('Um novo usuário se registrou e aguarda aprovação.'),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[admin.email],
                html_message=html_message
            )
    
    # Se o usuário foi aprovado
    if instance.is_approved and instance.approval_date:
        context = {'user': instance}
        html_message = render_to_string(
            'usuarios/email/approval_notification.html',
            context
        )
        
        send_mail(
            subject=_('Sua conta foi aprovada'),
            message=_('Sua conta no Observatório foi aprovada.'),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            html_message=html_message
        )

@receiver(pre_save, sender=CustomUser)
def check_approval_changes(sender, instance, **kwargs):
    """
    Monitora mudanças no status de aprovação
    """
    if instance.pk:  # Se não é uma nova instância
        old_instance = CustomUser.objects.get(pk=instance.pk)
        if not old_instance.is_approved and instance.is_approved:
            instance.record_approval()

@receiver(post_save, sender=OperatorProfile)
def notify_license_expiry(sender, instance, **kwargs):
    """
    Notifica quando a licença do operador está próxima do vencimento
    """
    if instance.license_expiry and instance.is_license_valid():
        # Lógica para verificar e notificar sobre vencimento próximo
        pass