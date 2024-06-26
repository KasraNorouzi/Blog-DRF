from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import User, Profile


# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('email', 'is_superuser', 'is_staff', 'is_active')
    search_fields = ('email', 'is_active')
    ordering = ('email',)
    fieldsets = (
        ('Authentication',
         {'fields':
              ('email', 'password')}),

        ('permissions', {'fields':
                        ('is_superuser', 'is_staff', 'is_active')}),

        ('group permissions', {'fields': (
            'groups', 'user_permissions'
        )}),

        ('important date', {'fields':
                            ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_superuser", "is_active",
            )}
         ),
    )


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)
