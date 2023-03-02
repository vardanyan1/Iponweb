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
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        fields = ("id", "user", "avatar", "registered_at")
        model = Customer
        read_only_fields = ("registered_at",)

    def to_representation(self, instance):
        user = instance.user

        user_data = UserSerializer(user).data

        representation = super().to_representation(instance)
        representation['user'] = user_data

        return representation


class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "photo")
        model = ItemsCategory


class StoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "photo")
        model = StoreCategory


class StoreOwnerSerializer(serializers.ModelSerializer):
    user = user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        fields = ("id", "user", "avatar", "registered_at")
        model = StoreOwner

    def to_representation(self, instance):
        user = instance.user

        user_data = UserSerializer(user).data

        representation = super().to_representation(instance)
        representation['user'] = user_data

        return representation


class StoreSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=StoreOwner.objects.all())
    store_category = serializers.PrimaryKeyRelatedField(queryset=StoreCategory.objects.all())

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
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    items = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=True)

    class Meta:
        model = MyBag
        fields = ("id", "customer", "items", "total_price")

    def to_representation(self, instance):
        customer = instance.customer
        items = instance.items.all()

        customer_data = CustomerSerializer(customer).data
        item_data = ItemSerializer(items, many=True).data

        representation = super().to_representation(instance)
        representation['customer'] = customer_data
        representation['items'] = item_data

        return representation


class PurchaseSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    items = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=True)

    class Meta:
        fields = ("id", "items", "buy_time", "customer", "total_price")
        model = Purchase

    def to_representation(self, instance):
        customer = instance.customer
        items = instance.items.all()

        customer_data = CustomerSerializer(customer).data
        item_data = ItemSerializer(items, many=True).data

        representation = super().to_representation(instance)
        representation['customer'] = customer_data
        representation['items'] = item_data

        return representation
