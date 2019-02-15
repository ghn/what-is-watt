from django.contrib import admin
from app.watt.models import Item, ItemCategory

class ItemAdmin(admin.ModelAdmin):
    pass

class ItemCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
