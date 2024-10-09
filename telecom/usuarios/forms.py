from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, OperatorProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'company', 'position', 'phone_number')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'company', 'position', 'phone_number')

class OperatorProfileForm(forms.ModelForm):
    class Meta:
        model = OperatorProfile
        fields = ('operator_name', 'license_number')

class UserApprovalForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('is_approved',)

class UserPermissionForm(forms.Form):
    VIEW_DATA = 'view_data'
    EDIT_DATA = 'edit_data'
    APPROVE_DATA = 'approve_data'
    
    PERMISSION_CHOICES = [
        (VIEW_DATA, 'View Data'),
        (EDIT_DATA, 'Edit Data'),
        (APPROVE_DATA, 'Approve Data'),
    ]
    
    permissions = forms.MultipleChoiceField(
        choices=PERMISSION_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )