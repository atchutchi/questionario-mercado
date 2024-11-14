# usuarios/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, OperatorProfile, UserPermission

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_approved', 
                   'is_operator', 'company', 'date_joined')
    list_filter = ('is_approved', 'is_operator', 'is_staff', 'operator_type', 
                  'date_joined', 'approval_date')
    search_fields = ('email', 'first_name', 'last_name', 'company')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'company', 'position', 'phone_number')
        }),
        (_('Operator info'), {
            'fields': ('is_operator', 'operator_type'),
            'classes': ('collapse',)
        }),
        (_('Approval status'), {
            'fields': ('is_approved', 'approval_date', 'approved_by', 'notes'),
            'classes': ('collapse',)
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    
    readonly_fields = ('approval_date', 'approved_by', 'date_joined', 'last_login')
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.approved_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(OperatorProfile)
class OperatorProfileAdmin(admin.ModelAdmin):
    list_display = ('operator_name', 'license_number', 'license_expiry', 
                   'is_active', 'registration_date')
    list_filter = ('is_active', 'license_expiry', 'registration_date')
    search_fields = ('operator_name', 'license_number', 'user__email')
    readonly_fields = ('registration_date', 'last_updated')
    
    fieldsets = (
        (_('Basic Information'), {
            'fields': ('user', 'operator_name', 'is_active')
        }),
        (_('License Information'), {
            'fields': ('license_number', 'license_expiry')
        }),
        (_('Service Areas'), {
            'fields': ('service_areas',)
        }),
        (_('Technical Contact'), {
            'fields': ('technical_contact',)
        }),
        (_('Metadata'), {
            'fields': ('registration_date', 'last_updated'),
            'classes': ('collapse',)
        }),
    )

@admin.register(UserPermission)
class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'permission_name', 'is_active', 'granted_at', 
                   'expires_at', 'granted_by')
    list_filter = ('permission_name', 'is_active', 'granted_at', 'expires_at')
    search_fields = ('user__email', 'description')
    readonly_fields = ('granted_at', 'granted_by')
    
    fieldsets = (
        (None, {
            'fields': ('user', 'permission_name', 'is_active')
        }),
        (_('Permission Details'), {
            'fields': ('description', 'expires_at')
        }),
        (_('Metadata'), {
            'fields': ('granted_at', 'granted_by'),
            'classes': ('collapse',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not change:  # Se é uma nova permissão
            obj.granted_by = request.user
        super().save_model(request, obj, form, change)