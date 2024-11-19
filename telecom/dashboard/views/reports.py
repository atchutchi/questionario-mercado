# dashboard/views/reports.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView

class ReportsView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard/reports.html'
    
    def test_func(self):
        return self.request.user.is_staff
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'reports'
        return context