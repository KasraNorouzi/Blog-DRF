from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User


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


admin.site.register(User, CustomUserAdmin)
