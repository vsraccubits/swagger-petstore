from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User


class UserAdmin(BaseUserAdmin):

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "phone",
        "user_status",
    )
    list_filter = ("user_status",)
    fieldsets = (
        ("Credentials", {"fields": ("username", "password")}),
        ("User details", {"fields": ("first_name", "last_name", "email", "phone")}),
        ("Account Status", {"fields": ("user_status",)}),
    )


admin.site.register(User, UserAdmin)
