from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser


@staff_member_required
def approve_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_approved = True
    user.save()
    # Adicione lógica para notificar o usuário
    return redirect('admin:auth_user_changelist')