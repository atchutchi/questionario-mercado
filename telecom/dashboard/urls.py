# dashboard/urls.py
from django.urls import path
from .views import main, analytics, reports

app_name = 'dashboard'

urlpatterns = [
    path('', main.DashboardView.as_view(), name='home'),
    path('analytics/', analytics.AnalyticsView.as_view(), name='analytics'),
    path('reports/', reports.ReportsView.as_view(), name='reports'),


    path('analytics/market/', MarketAnalyticsView.as_view(), name='market-analytics'),
    path('analytics/traffic/', TrafficAnalyticsView.as_view(), name='traffic-analytics'),
    path('analytics/revenue/', RevenueAnalyticsView.as_view(), name='revenue-analytics'),
    path('reports/export/', ExportReportView.as_view(), name='export-report'),
]
