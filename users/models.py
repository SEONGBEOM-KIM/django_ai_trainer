from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other")
    )

    NUMBER_FIRST = "1"
    NUMBER_SECOND = "2"
    NUMBER_THIRD = "3"
    NUMBER_FOURTH = "4"
    NUMBER_FIFTH = "5"
    NUMBER_SIXTH = "6"

    NUMBER_CHOICES = (
        (NUMBER_FIRST, "1"),
        (NUMBER_SECOND, "2"),
        (NUMBER_THIRD, "3"),
        (NUMBER_FOURTH, "4"),
        (NUMBER_FIFTH, "5"),
        (NUMBER_SIXTH, "6"),
    )

    name = models.CharField(max_length=20, blank=True)
    school = models.CharField(max_length=10, blank=True)
    grade = models.CharField(choices=NUMBER_CHOICES,
                             max_length=10, default=NUMBER_FIRST)
    group = models.CharField(choices=NUMBER_CHOICES, max_length=10, blank=True)
    number = models.CharField(max_length=2, blank=True)
    age = models.CharField(max_length=10, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    teacher = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
