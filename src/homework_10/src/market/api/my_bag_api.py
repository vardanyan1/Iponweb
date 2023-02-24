import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.generic import View

from ..shop.models.my_bag_model import MyBag
from ..shop.models.customer_model import Customer
from ..shop.models.item_model import Item
from ..tools.sending_tools import data_status, ok_status
from ..serializers.my_bag_serializer import my_bag_serializer


class MyBagView(View):
    @staticmethod
    def get(request):
        bags = MyBag.objects.all()
        data = []
        for bag in bags:
            data.append(my_bag_serializer(bag))

        return data_status(data=data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        customer_id = data['customer']
        try:
            customer = Customer.objects.get(id=customer_id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "customer_not_found"})

        items_ids = data['items']
        items = []
        for item_id in items_ids:
            try:
                item = Item.objects.get(id=item_id)
                items.append(item)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "item_not_found"})

        total_price = float(data['total_price'])

        my_bag = MyBag.objects.create(customer=customer, total_price=total_price)
        my_bag.items.set(items)
        my_bag.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return MyBagView.get_single(request, id)
        if request.method == "DELETE":
            return MyBagView.delete(request, id)
        if request.method == "PATCH":
            return MyBagView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            my_bag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "my_bag_not_found"})
        return data_status(my_bag_serializer(my_bag))

    @staticmethod
    def delete(request, id):
        try:
            my_bag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "my_bag_not_found"})

        my_bag.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)

        try:
            my_bag = MyBag.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "my_bag_not_found"})

        if "customer" in data:
            customer_id = data['customer']
            try:
                customer = Customer.objects.get(id=customer_id)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "customer_not_found"})

            my_bag.customer = customer

        if "items" in data:
            items_ids = data['items']
            items = []
            for item_id in items_ids:
                try:
                    item = Item.objects.get(id=item_id)
                    items.append(item)
                except ObjectDoesNotExist:
                    return JsonResponse({"status": "item_not_found"})
            my_bag.items.set(items)

        if "total_price" in data:
            total_price = data['total_price']
            my_bag.total_price = total_price

        my_bag.save()
        return ok_status()
