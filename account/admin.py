from django.contrib import admin
from .models import User 

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserAdmin(BaseUserAdmin):
 
    list_display = ["id","email", "first_name","last_name","organization", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["first_name","last_name","organization"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "first_name","last_name","organization","password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email","id"]
    filter_horizontal = []

admin.site.register(User, UserAdmin)
