from django import forms
from allauth.account.forms import SignupForm
from .models import UserProfile

class CustomSignupForm(SignupForm):
    # Adicione campos adicionais conforme necessário

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user_profile = UserProfile.objects.create(user=user)
        user_profile.save()
        return user