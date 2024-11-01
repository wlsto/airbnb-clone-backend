from django.db import models
from common.models import CommonModel


# Create your models here.
class Room(CommonModel):
    """Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE = "entire", "Entire"
        PRIVATE = "private", "Private"
        SHARE = "share", "Share"

    country = models.CharField(
        max_length=50,
        default="South Korea",
    )
    city = models.CharField(
        max_length=80,
        default="Seoul",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=False,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices,
    )
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
    )


class Amenity(CommonModel):
    """Amenity Class Definition"""

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        null=True,
    )
