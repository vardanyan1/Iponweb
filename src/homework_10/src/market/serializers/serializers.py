from rest_framework import serializers
from ..shop.models.customer_model import Customer
from ..shop.models.items_category_model import ItemsCategory
from ..shop.models.item_model import Item
from ..shop.models.store_category_model import StoreCategory
from ..shop.models.store_owner_model import StoreOwner
from ..shop.models.store_model import Store
from ..shop.models.my_bag_model import MyBag
from ..shop.models.purchase_model import Purchase
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "username", "email", "first_name", "last_name")
        model = User


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        fields = ("id", "user", "avatar", "registered_at")
        model = Customer


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "photo")
        model = ItemsCategory


class StoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "photo")
        model = StoreCategory


class StoreOwnerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        fields = ("id", "user", "avatar", "registered_at")
        model = StoreOwner


class StoreSerializer(serializers.ModelSerializer):
    owner = StoreOwnerSerializer(many=False)
    store_category = StoreCategorySerializer(many=False)

    class Meta:
        fields = ("id", "name", "owner", "store_category")
        model = Store


class ItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=ItemsCategory.objects.all())
    store = serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())

    class Meta:
        fields = ("id", "name", "picture", "category", "price", "quantity", "info", "store")
        model = Item


class MyBagSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False)
    items = ItemSerializer(many=True)

    class Meta:
        fields = ("id", "customer", "items", "total_price")
        model = MyBag


class PurchaseSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(many=False)
    items = ItemSerializer(many=True)

    class Meta:
        fields = ("id", "items", "buy_time", "customer", "total_price")
        model = Purchase
