from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class Photo(core_models.TimeStampedModel):
    """ Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item Definition """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """ Room Type Definition"""

    class Meta:
        verbose_name = "Room Type"
        ordering = ["-created"]


class Facilty(AbstractItem):

    """Facility Type definition"""

    class Meta:
        verbose_name = "Facilitie"


class Amenity(AbstractItem):

    """Amenity Type definition"""

    class Meta:
        verbose_name = "Amenitie"


class HouseRule(AbstractItem):

    """HouseRule Type definition"""

    class Meta:
        verbose_name = "House Rules"


class Room(core_models.TimeStampedModel):

    """ Room Model Definition"""

    name = models.CharField(max_length=80)
    description = models.TextField(max_length=140)
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    guests = models.IntegerField()
    address = models.CharField(max_length=140)

    check_in = models.TimeField()
    check_out = models.TimeField()
    beds = models.IntegerField()
    badrooms = models.IntegerField()
    baths = models.IntegerField()
    instant_room = models.BooleanField(default=False)

    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    Facilties = models.ManyToManyField("Facilty", blank=True)

    def __str__(self):
        return self.name
