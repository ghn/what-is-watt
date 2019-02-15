from django.db import models
from django_enumfield import enum


class EnergyType(enum.Enum):
    ELECTRIC = 0

    labels = {
        ELECTRIC: 'Electrical'
    }


class ItemCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class ItemManager(models.Manager):
    pass


class Item(models.Model):
    name = models.CharField(max_length=200)
    wh_per_unit = models.PositiveIntegerField()
    category = models.ForeignKey(ItemCategory,
                                 on_delete=models.CASCADE,
                                 related_name="items",
                                 null=True)
    energy_type = enum.EnumField(EnergyType, default=EnergyType.ELECTRIC)
    unit = models.CharField(max_length=10, null=True)
    default_usage = models.FloatField(default=1)
    source = models.CharField(max_length=512, null=True)

    objects = ItemManager()

    def __str__(self):
        return self.name

    def string_value(self):
        return "{} kw/{}".format(self.wh_per_unit, self.unit)

