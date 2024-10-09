from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile

@staff_member_required
def approve_user(request, user_id):
    profile = get_object_or_404(UserProfile, user__id=user_id)
    profile.is_approved = True
    profile.save()
    # Adicione lógica para notificar o usuário
    return redirect('admin:auth_user_changelist')