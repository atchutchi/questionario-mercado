from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone

class CustomUser(AbstractUser):
    """
    Modelo de usuário personalizado para o Observatório do Mercado das Telecomunicações.
    Estende o modelo de usuário padrão do Django com campos adicionais específicos.
    """
    # Campos base
    email = models.EmailField(
        _('email address'),
        unique=True,
        error_messages={
            'unique': _("Este email já está registrado no sistema."),
        }
    )
    
    # Campos de grupos e permissões atualizados
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='custom_user_groups',
        related_query_name='custom_user'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_user_permissions',
        related_query_name='custom_user'
    )
    
    # Status e aprovação
    is_approved = models.BooleanField(
        _('approved'),
        default=False,
        help_text=_('Indica se este usuário foi aprovado por um administrador.')
    )
    approval_date = models.DateTimeField(
        _('approval date'),
        null=True,
        blank=True
    )
    approved_by = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='approved_users'
    )
    
    # Informações profissionais
    company = models.CharField(
        _('empresa'),
        max_length=100,
        blank=True,
        help_text=_('Nome da empresa ou organização')
    )
    position = models.CharField(
        _('cargo'),
        max_length=100,
        blank=True,
        help_text=_('Cargo ou posição na empresa')
    )
    phone_number = models.CharField(
        _('telefone'),
        max_length=20,
        blank=True,
        help_text=_('Número de telefone para contato')
    )
    
    # Tipo de usuário
    is_operator = models.BooleanField(
        _('operador'),
        default=False,
        help_text=_('Indica se este usuário é um operador de telecomunicações')
    )
    operator_type = models.CharField(
        _('tipo de operador'),
        max_length=50,
        choices=[
            ('MOBILE', _('Operador Móvel')),
            ('FIXED', _('Operador Fixo')),
            ('ISP', _('Provedor de Internet')),
            ('MVNO', _('Operador Móvel Virtual')),
        ],
        blank=True,
        null=True
    )
    
    # Campos de auditoria
    last_activity = models.DateTimeField(
        _('última atividade'),
        null=True,
        blank=True
    )
    notes = models.TextField(
        _('notas'),
        blank=True,
        help_text=_('Notas administrativas sobre o usuário')
    )
    
    # Configurações da conta
    require_password_change = models.BooleanField(
        _('requer mudança de senha'),
        default=False
    )
    account_locked = models.BooleanField(
        _('conta bloqueada'),
        default=False
    )
    failed_login_attempts = models.PositiveIntegerField(
        _('tentativas de login falhas'),
        default=0
    )

    class Meta:
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')
        permissions = [
            ("approve_user", "Can approve user registration"),
            ("view_dashboard", "Can view dashboard"),
            ("manage_operators", "Can manage operators"),
        ]

    def __str__(self):
        return self.get_full_name() or self.email

    def get_full_name(self):
        """Retorna o nome completo do usuário."""
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name or self.email

    def approve(self, approved_by=None):
        """Aprova o usuário."""
        self.is_approved = True
        self.approval_date = timezone.now()
        self.approved_by = approved_by
        self.save()

    def lock_account(self):
        """Bloqueia a conta do usuário."""
        self.account_locked = True
        self.save()

    def unlock_account(self):
        """Desbloqueia a conta do usuário."""
        self.account_locked = False
        self.failed_login_attempts = 0
        self.save()

    def record_login_attempt(self, success):
        """Registra uma tentativa de login."""
        if success:
            self.failed_login_attempts = 0
            self.last_activity = timezone.now()
        else:
            self.failed_login_attempts += 1
            if self.failed_login_attempts >= 5:
                self.lock_account()
        self.save()

    def update_last_activity(self):
        """Atualiza o timestamp da última atividade."""
        self.last_activity = timezone.now()
        self.save()

class OperatorProfile(models.Model):
    """
    Perfil adicional para usuários que são operadores de telecomunicações.
    """
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='operator_profile'
    )
    operator_name = models.CharField(
        _('nome do operador'),
        max_length=100
    )
    license_number = models.CharField(
        _('número da licença'),
        max_length=50,
        unique=True
    )
    license_expiry = models.DateField(
        _('validade da licença'),
        null=True,
        blank=True
    )
    service_areas = models.JSONField(
        _('áreas de serviço'),
        default=list,
        help_text=_('Regiões onde o operador atua')
    )
    technical_contact = models.JSONField(
        _('contato técnico'),
        default=dict,
        help_text=_('Informações do contato técnico')
    )
    is_active = models.BooleanField(
        _('ativo'),
        default=True
    )
    registration_date = models.DateTimeField(
        _('data de registro'),
        auto_now_add=True
    )
    last_updated = models.DateTimeField(
        _('última atualização'),
        auto_now=True
    )

    class Meta:
        verbose_name = _('perfil de operador')
        verbose_name_plural = _('perfis de operadores')
        ordering = ['-registration_date']

    def __str__(self):
        return f"{self.operator_name} ({self.license_number})"

    def clean(self):
        """Validação personalizada do modelo."""
        if self.license_expiry and self.license_expiry < timezone.now().date():
            raise ValidationError({
                'license_expiry': _('A licença não pode ter expirado.')
            })

    def is_license_valid(self):
        """Verifica se a licença está válida."""
        if not self.license_expiry:
            return False
        return self.license_expiry >= timezone.now().date()

    def get_service_areas_display(self):
        """Retorna as áreas de serviço formatadas."""
        return ", ".join(self.service_areas)

class UserPermission(models.Model):
    """
    Permissões personalizadas para usuários do sistema.
    """
    # Constantes para tipos de permissão
    VIEW_DATA = 'view_data'
    EDIT_DATA = 'edit_data'
    APPROVE_DATA = 'approve_data'
    MANAGE_OPERATORS = 'manage_operators'
    GENERATE_REPORTS = 'generate_reports'
    
    PERMISSION_CHOICES = [
        (VIEW_DATA, _('Visualizar Dados')),
        (EDIT_DATA, _('Editar Dados')),
        (APPROVE_DATA, _('Aprovar Dados')),
        (MANAGE_OPERATORS, _('Gerenciar Operadores')),
        (GENERATE_REPORTS, _('Gerar Relatórios')),
    ]

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='permissions'
    )
    permission_name = models.CharField(
        _('nome da permissão'),
        max_length=100,
        choices=PERMISSION_CHOICES
    )
    description = models.TextField(
        _('descrição'),
        blank=True
    )
    granted_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='permissions_granted'
    )
    granted_at = models.DateTimeField(
        _('concedido em'),
        auto_now_add=True
    )
    expires_at = models.DateTimeField(
        _('expira em'),
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        _('ativo'),
        default=True
    )

    class Meta:
        verbose_name = _('permissão de usuário')
        verbose_name_plural = _('permissões de usuário')
        unique_together = ('user', 'permission_name')
        ordering = ['-granted_at']

    def __str__(self):
        return f"{self.user.email} - {self.get_permission_name_display()}"

    def is_valid(self):
        """Verifica se a permissão está válida."""
        if not self.is_active:
            return False
        if self.expires_at and self.expires_at < timezone.now():
            return False
        return True