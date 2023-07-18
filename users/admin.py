from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # list_display = ["email", "name", "is_active"]
    fieldsets = (
        
        (_("Personal info"), {"fields": ("first_name", "last_name", "name", "email")}),
        (None, {"fields": ("password",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("password1", "password2"),
            },
        ),
    )
    ordering = ("email",)
