# usuarios/urls.py
from django.urls import path
from .views import (
   approvals,
   dashboard,
   operators,
   permissions,
   profiles
)

app_name = 'usuarios'

urlpatterns = [
   # Dashboard URLs
   path('', dashboard.UserDashboardView.as_view(), name='user_dashboard'),
   path('admin-dashboard/', dashboard.AdminDashboardView.as_view(), name='admin_dashboard'),

   # Approval URLs
   path('approvals/', approvals.PendingApprovalListView.as_view(), name='pending_approval_list'),
   path('approvals/<int:pk>/review/', approvals.UserApprovalView.as_view(), name='user_approval'),

   # Operator URLs
   path('operators/', operators.OperatorListView.as_view(), name='operator_list'),
   path('operators/create/', operators.OperatorProfileCreateView.as_view(), name='operator_create'),
   path('operators/<int:pk>/edit/', operators.OperatorProfileUpdateView.as_view(), name='operator_edit'),
   path('operators/<int:pk>/', operators.OperatorProfileDetailView.as_view(), name='operator_detail'),

   # Permission URLs
   path('permissions/', permissions.PermissionListView.as_view(), name='permission_list'),
   path('permissions/create/<int:user_id>/', permissions.PermissionCreateView.as_view(), name='permission_create'),
   path('permissions/<int:pk>/edit/', permissions.PermissionUpdateView.as_view(), name='permission_edit'),
   path('permissions/<int:pk>/delete/', permissions.PermissionDeleteView.as_view(), name='permission_delete'),

   # Profile URLs
   path('profile/', profiles.ProfileDetailView.as_view(), name='profile_view'),
   path('profile/edit/', profiles.ProfileUpdateView.as_view(), name='profile_edit'),

   # Email Confirmation
   path('approve-email/<str:key>/', profiles.ApproveEmailView.as_view(), name='approve_email'),

   # Custom Authentication URLs
   path('login/', profiles.CustomLoginView.as_view(), name='login'),
   path('logout/', profiles.CustomLogoutView.as_view(), name='logout'),
   path('password/change/', profiles.CustomPasswordChangeView.as_view(), name='change_password'),
   path('password/reset/', profiles.CustomPasswordResetView.as_view(), name='password_reset'),
   path('password/reset/confirm/<uidb64>/<token>/', 
       profiles.CustomPasswordResetConfirmView.as_view(), 
       name='password_reset_confirm'
   ),

   # Additional Profile Management
   path('change-email/', profiles.ChangeEmailView.as_view(), name='change_email'),
   path('profile/delete/', profiles.DeleteAccountView.as_view(), name='delete_account'),

   # Help and Support
   path('help-center/', profiles.HelpCenterView.as_view(), name='help_center'),

   # API URLs (se necessário para interações AJAX)
   path('api/validate-email/', profiles.ValidateEmailView.as_view(), name='validate_email'),
   path('api/check-username/', profiles.CheckUsernameView.as_view(), name='check_username'),
   path('api/update-notification-settings/', profiles.UpdateNotificationSettingsView.as_view(), 
        name='update_notification_settings'),
]

# Configurar handler404 e handler500 personalizados
handler404 = 'usuarios.views.profiles.custom_404'
handler500 = 'usuarios.views.profiles.custom_500'