from django.db import models
from users import models as user_models


class AbstractItem(models.Model):

    """ Abstract Item Model Definition """

    name = models.CharField(max_length=80, blank=True)

    class Meta:
        abstract = True


class MeasurementItem(AbstractItem):

    pass


class Event(models.Model):

    """ Event Model Definition """

    events = models.ManyToManyField(MeasurementItem, blank=True)
