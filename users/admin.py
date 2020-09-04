from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin"""

    fieldsets = (
        (
            "Custom Profile",
            {
                "fields": (
                    "gender",
                    "birthdate",
                    "avatar",
                    "lang",
                    "currency",
                    "bio",
                    "superhost",
                )
            },
        ),
    ) + UserAdmin.fieldsets
