from django.contrib import admin
from . import models


@admin.register(models.MeasurementItem)
class MeasurementItemAdmin(admin.ModelAdmin):

    """ Measurement Item Admin Definition """

    list_display = ("name",)


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):

    """ Event Admin Definition """

    pass
