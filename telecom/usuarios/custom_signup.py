# usuarios/custom_signup.py
from django import forms
from django.contrib.auth import get_user_model

class CustomSignupForm(forms.Form):
    company = forms.CharField(max_length=100, required=False)
    position = forms.CharField(max_length=100, required=False)
    phone_number = forms.CharField(max_length=20, required=False)

    def signup(self, request, user):
        user.company = self.cleaned_data['company']
        user.position = self.cleaned_data['position']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()