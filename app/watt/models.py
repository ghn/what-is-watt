from django.db import models


class ItemManager(models.Manager):
    pass

class Item(models.Model):
    name = models.CharField(max_length=200)
    power = models.PositiveIntegerField()
    power_type = models.CharField(max_length=200)

    objects = ItemManager()

    def __str__(self):
        return self.name
