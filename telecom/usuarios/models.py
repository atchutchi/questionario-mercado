from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # Campos base
    email = models.EmailField(_('email address'), unique=True)
    is_approved = models.BooleanField(
        _('approved'),
        default=False,
        help_text=_('Designates whether this user has been approved by an admin.')
    )
    
    # Informações profissionais
    company = models.CharField(
        _('company'),
        max_length=100,
        blank=True,
        help_text=_('Company or organization name')
    )
    position = models.CharField(
        _('position'),
        max_length=100,
        blank=True,
        null=True,
        help_text=_('Job position or title')
    )
    phone_number = models.CharField(
        _('phone number'),
        max_length=20,
        blank=True,
        null=True,
        help_text=_('Contact phone number')
    )

    # Campos relacionados ao operador
    is_operator = models.BooleanField(
        _('operator status'),
        default=False,
        help_text=_('Designates whether this user is a telecom operator.')
    )
    
    # Configurações do modelo
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-date_joined']

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.email

class OperatorProfile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='operator_profile'
    )
    operator_name = models.CharField(
        _('operator name'),
        max_length=100
    )
    license_number = models.CharField(
        _('license number'),
        max_length=50,
        unique=True
    )
    is_active = models.BooleanField(
        _('active'),
        default=True
    )
    registration_date = models.DateTimeField(
        _('registration date'),
        auto_now_add=True
    )
    last_updated = models.DateTimeField(
        _('last updated'),
        auto_now=True
    )

    class Meta:
        verbose_name = _('operator profile')
        verbose_name_plural = _('operator profiles')
        ordering = ['-registration_date']

    def __str__(self):
        return f"{self.operator_name} - {self.license_number}"

class UserPermission(models.Model):
    # Constantes para permissões
    VIEW_DATA = 'view_data'
    EDIT_DATA = 'edit_data'
    APPROVE_DATA = 'approve_data'
    
    PERMISSION_CHOICES = [
        (VIEW_DATA, _('View Data')),
        (EDIT_DATA, _('Edit Data')),
        (APPROVE_DATA, _('Approve Data')),
    ]

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='permissions'
    )
    permission_name = models.CharField(
        _('permission name'),
        max_length=100,
        choices=PERMISSION_CHOICES
    )
    description = models.TextField(
        _('description'),
        blank=True
    )
    granted_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='permissions_granted'
    )
    granted_at = models.DateTimeField(
        _('granted at'),
        auto_now_add=True
    )

    class Meta:
        verbose_name = _('user permission')
        verbose_name_plural = _('user permissions')
        unique_together = ('user', 'permission_name')
        ordering = ['-granted_at']

    def __str__(self):
        return f"{self.user.email} - {self.get_permission_name_display()}"