from django.db import models
from users import models as user_models


class Stat(models.Model):

    """ Stats Model Definition """

    name = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, blank=True)
    pacer = models.IntegerField(blank=True)
    longTimeRun = models.IntegerField(blank=True)
    stepTest = models.IntegerField(blank=True)
    bendFoward = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True)
    shoulder = models.IntegerField(blank=True)
    upperBody = models.IntegerField(blank=True)
    side = models.IntegerField(blank=True)
    lowerBody = models.IntegerField(blank=True)
    totalFlexibility = models.IntegerField(blank=True)
    pushUp = models.IntegerField(blank=True)
    sitUp = models.IntegerField(blank=True)
    grip = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True)
    sprint = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True)
    longJump = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True)
    height = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True)
    weight = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True)
    fat = models.DecimalField(
        max_digits=5, decimal_places=1, blank=True)
