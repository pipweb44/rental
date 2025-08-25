from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'is_verified', 'created_at')
    list_filter = ('user_type', 'is_verified', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone')

    fieldsets = UserAdmin.fieldsets + (
        ('معلومات إضافية', {
            'fields': ('user_type', 'phone', 'address', 'profile_image', 'is_verified')
        }),
    )
