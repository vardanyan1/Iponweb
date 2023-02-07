from django.contrib import admin
from .models import StoreCategory, ItemsCategory, Customer


class StoreAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(StoreCategory, StoreAdmin)
admin.site.register(ItemsCategory, ItemAdmin)
admin.site.register(Customer, CustomerAdmin)
