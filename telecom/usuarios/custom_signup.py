# usuarios/custom_signup.py
from django import forms
from allauth.account.forms import SignupForm
from django.utils.translation import gettext_lazy as _

class CustomSignupForm(SignupForm):
    company = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': _('Company Name'), 'class': 'form-control'}
        )
    )
    position = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': _('Job Position'), 'class': 'form-control'}
        )
    )
    phone_number = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': _('Phone Number'), 'class': 'form-control'}
        )
    )

    def save(self, request):
        user = super().save(request)
        user.company = self.cleaned_data.get('company', '')
        user.position = self.cleaned_data.get('position', '')
        user.phone_number = self.cleaned_data.get('phone_number', '')
        user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and email.split('@')[1] not in ['arn.gw', 'gmail.com']:
            raise forms.ValidationError(
                _('Please use your company email address or Gmail account.')
            )
        return email