from django.contrib import admin
from app.watt.models import Item

class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)
