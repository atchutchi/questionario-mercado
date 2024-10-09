from django.shortcuts import redirect
from django.urls import reverse

class ApprovalMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_approved:
            if request.path != reverse('account_logout'):
                return redirect('account_login')
        return self.get_response(request)