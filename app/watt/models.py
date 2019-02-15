from django.db import models


class ItemManager(models.Manager):
    pass

class Item(models.Model):
    name = models.CharField(max_length=200)
    wh_per_unit = models.PositiveIntegerField()
    energy_type = models.CharField(max_length=200)
    unit = models.CharField(max_length=10, null=True)
    default_usage = models.FloatField(default=1)
    source = models.CharField(max_length=512, null=True)

    objects = ItemManager()

    def __str__(self):
        return self.name

    def string_value(self):
        return "{} kw/{}".format(self.wh_per_unit, self.unit)
