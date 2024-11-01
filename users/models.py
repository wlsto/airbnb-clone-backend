from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoicies(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        # ()를 하건 안하던 똑같음
        WON = ("krw", "Korean Won")
        USD = "usd", "Dollar"

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    avatar = models.ImageField(
        blank=True,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    is_host = models.BooleanField(
        default=False,
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoicies,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices,
    )
