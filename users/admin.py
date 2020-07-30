from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": ("name", "school", "grade", "group", "number", "gender", "age", "teacher", "bio")
            }
        ),
    )

    list_display = ("username", "name", "school", "grade", "group", "number",
                    "gender", "age", "teacher",)

    list_filter = ("school", "gender", "grade",)

    search_fields = ("name", "school", )
