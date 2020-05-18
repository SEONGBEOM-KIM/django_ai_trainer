from django.contrib import admin
from . import models


@admin.register(models.Stat)
class StatAdmin(admin.ModelAdmin):

    """ Stat Admin """

    list_display = ("name", "pacer", "longTimeRun", "stepTest", "bendFoward", "shoulder", "upperBody", "side", "lowerBody",
                    "totalFlexibility", "pushUp", "sitUp", "grip", "sprint", "longJump", "height", "weight", "fat")

    fieldsets = (
        (
            "PAPS Stats",
            {
                "fields": ("name", "pacer", "longTimeRun", "stepTest", "bendFoward", "shoulder", "upperBody", "side", "lowerBody",
                           "totalFlexibility", "pushUp", "sitUp", "grip", "sprint", "longJump", "height", "weight", "fat")
            }
        ),
    )
