import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.generic import View

from ..shop.models.item_model import Item
from ..shop.models.items_category_model import ItemsCategory
from ..shop.models.store_model import Store
from ..tools.sending_tools import data_status, ok_status
from ..serializers.item_serializer import item_serializer


class ItemView(View):
    @staticmethod
    def get(request):
        items = Item.objects.all()
        data = []
        for item in items:
            data.append(item_serializer(item))

        return data_status(data=data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        name = data['name']
        category_id = data['category']
        price = data['price']
        quantity = data['quantity']
        info = data['info']
        store_id = data['store']

        try:
            category = ItemsCategory.objects.get(id=category_id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "item_category_not_found"})
        try:
            store = Store.objects.get(id=store_id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "store_category_not_found"})

        item = Item.objects.create(
            name=name,
            category=category,
            price=price,
            quantity=quantity,
            info=info,
            store=store,
        )

        item.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemView.get_single(request, id)
        if request.method == "DELETE":
            return ItemView.delete(request, id)
        if request.method == "PATCH":
            return ItemView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "item_not_found"})
        return data_status(item_serializer(item))

    @staticmethod
    def delete(request, id):
        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "item_not_found"})

        item.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)

        try:
            item = Item.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "item_not_found"})

        if "name" in data:
            item.name = data['name']
        if "category" in data:
            try:
                category = ItemsCategory.objects.get(id=data['category'])
            except ObjectDoesNotExist:
                return JsonResponse({"status": "category_not_found"})
            item.category = category
        if "price" in data:
            item.price = data['price']
        if "quantity" in data:
            item.quantity = data['quantity']
        if "info" in data:
            item.info = data['info']
        if "store" in data:
            try:
                store = Store.objects.get(id=data['store'])
            except ObjectDoesNotExist:
                return JsonResponse({"status": "store_not_found"})
            item.store = store

        item.save()
        return ok_status()
