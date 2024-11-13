from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, OperatorProfile, UserPermission

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'company', 'position', 'phone_number')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'company', 'position', 'phone_number', 'is_approved')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class OperatorProfileForm(forms.ModelForm):
    class Meta:
        model = OperatorProfile
        fields = ('operator_name', 'license_number')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_license_number(self):
        license_number = self.cleaned_data.get('license_number')
        if OperatorProfile.objects.filter(license_number=license_number).exists():
            raise forms.ValidationError(_('This license number is already registered.'))
        return license_number

class UserPermissionForm(forms.ModelForm):
    class Meta:
        model = UserPermission
        fields = ('permission_name', 'description')
        widgets = {
            'permission_name': forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['permission_name'].widget.attrs['class'] = 'form-check-input'