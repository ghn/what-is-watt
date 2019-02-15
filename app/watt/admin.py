from django.contrib import admin
from app.watt.models import Item, ItemCategory

class ItemAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ("name", "category", "wh_per_unit", "unit", "energy_type", "default_usage")

class ItemCategoryAdmin(admin.ModelAdmin):
    ordering = ["name"]

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
