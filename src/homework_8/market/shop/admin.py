from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html

from .models import StoreCategory, ItemsCategory, Customer, StoreOwner, Store, Item


class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo_name')

    @admin.display(description='Photo')
    def photo_name(self, obj):
        if obj.photo:
            return format_html('<b><a href="{}">...{}</a></b>', obj.photo.url, obj.photo.name[-12:])


class ItemsCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo_name')

    @admin.display(description='Photo')
    def photo_name(self, obj):
        if obj.photo:
            return format_html('<b><a href="{}">...{}</a></b>', obj.photo.url, obj.photo.name[-12:])


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username_ref', 'name', 'surname', 'avatar_name', 'registered_at')

    @admin.display(description='Avatar')
    def avatar_name(self, obj):
        if obj.avatar:
            return format_html('<b><a href="{}">...{}</a></b>', obj.avatar.url, obj.avatar.name[-12:])

    @admin.display(description='Username')
    def username_ref(self, obj):
        link = f"/admin/shop/customer/{obj.id}/change/"
        return format_html('<b><a href="{}">{}</a></b>', link, obj.user.username)

    @admin.display(description='Name')
    def name(self, obj):
        return obj.user.first_name

    @admin.display(description='Surname')
    def surname(self, obj):
        return obj.user.last_name


class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar_name', 'registered_at')

    @admin.display(description='Avatar')
    def avatar_name(self, obj):
        if obj.avatar:
            return format_html('<b><a href="{}">...{}</a></b>', obj.avatar.url, obj.avatar.name[-12:])

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'store_owner_name', 'store_category_name')

    @admin.display(description="Owner")
    def store_owner_name(self, obj):
        link = f"/admin/shop/storeowner/{obj.owner.user.id}/change/"
        return format_html('<b><a href="{}">{}</a></b>', link, obj.owner.user)

    @admin.display(description="Store Category")
    def store_category_name(self, obj):
        link = f"/admin/shop/storecategory/{obj.store_category.id}/change/"
        return format_html('<b><a href="{}">{}</a></b>', link, obj.store_category.name)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'item_category_ref', 'image_name', 'store_ref', 'price', 'quantity', 'info')

    @admin.display(description='Image')
    def image_name(self, obj):
        if obj.picture:
            return format_html('<b><a href="{}">...{}</a></b>', obj.picture.url, obj.picture.name[-12:])

    @admin.display(description='Items Cat.')
    def item_category_ref(self, obj):
        link = f"/admin/shop/itemscategory/{obj.category.id}/change/"
        return format_html('<b><a href="{}">{}</a></b>', link, obj.category.name)

    @admin.display(description="Store")
    def store_ref(self, obj):
        link = f"/admin/shop/store/{obj.store.id}/change/"
        return format_html('<b><a href="{}">{}</a></b>', link, obj.store.name)


admin.site.register(StoreCategory, StoreCategoryAdmin)
admin.site.register(ItemsCategory, ItemsCategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(StoreOwner, StoreOwnerAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Item, ItemAdmin)
