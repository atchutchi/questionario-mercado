# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, OperatorProfile, UserPermission

class CustomUserCreationForm(UserCreationForm):
    """
    Formulário para criação de novo usuário com campos personalizados.
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'company', 'position', 
                 'phone_number', 'is_operator', 'operator_type')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Torna campos obrigatórios
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['company'].required = True
        
        # Adiciona classes Bootstrap
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            
        # Customiza o campo operator_type
        self.fields['operator_type'].widget = forms.Select(
            choices=CustomUser.operator_type.field.choices,
            attrs={'class': 'form-control', 'disabled': not self.initial.get('is_operator')}
        )

    def clean(self):
        cleaned_data = super().clean()
        is_operator = cleaned_data.get('is_operator')
        operator_type = cleaned_data.get('operator_type')
        
        if is_operator and not operator_type:
            raise forms.ValidationError(
                _('Operadores devem especificar um tipo de operação.')
            )
        return cleaned_data

class CustomUserChangeForm(UserChangeForm):
    """
    Formulário para edição de usuário existente.
    """
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'company', 'position', 
                 'phone_number', 'is_operator', 'operator_type')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class OperatorProfileForm(forms.ModelForm):
    """
    Formulário para criação e edição de perfil de operador.
    """
    class Meta:
        model = OperatorProfile
        fields = ('operator_name', 'license_number', 'license_expiry', 
                 'service_areas', 'technical_contact')
        widgets = {
            'license_expiry': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'service_areas': forms.SelectMultiple(
                attrs={'class': 'form-control'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['service_areas']:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

        # Configura o campo technical_contact como um conjunto de subcampos
        self.fields['technical_contact'] = forms.JSONField(
            widget=forms.HiddenInput(),
            required=False
        )

class UserPermissionForm(forms.ModelForm):
    """
    Formulário para gestão de permissões de usuário.
    """
    class Meta:
        model = UserPermission
        fields = ('permission_name', 'description', 'expires_at')
        widgets = {
            'expires_at': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class UserApprovalForm(forms.Form):
    """
    Formulário para aprovação de usuários pendentes.
    """
    approve = forms.BooleanField(required=False)
    notes = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})