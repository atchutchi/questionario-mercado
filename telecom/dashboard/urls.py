# dashboard/urls.py
from django.urls import path
from .views import main, analytics, reports

app_name = 'dashboard'

urlpatterns = [
    path('', main.DashboardView.as_view(), name='home'),
    path('analytics/', analytics.AnalyticsView.as_view(), name='analytics'),
    path('reports/', reports.ReportsView.as_view(), name='reports'),
]
