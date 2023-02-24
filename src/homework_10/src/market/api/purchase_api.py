import json
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.generic import View

from ..shop.models.customer_model import Customer
from ..shop.models.item_model import Item
from ..shop.models.purchase_model import Purchase
from ..tools.sending_tools import data_status, ok_status
from ..serializers.purchase_serializer import purchase_serializer


class PurchaseView(View):
    @staticmethod
    def get(request):
        purchases = Purchase.objects.all()
        data = []
        for purchase in purchases:
            data.append(purchase_serializer(purchase))

        return data_status(data=data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        items_ids = data['items']
        items = []
        for item_id in items_ids:
            try:
                item = Item.objects.get(id=item_id)
                items.append(item)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "item_not_found"})

        try:
            buy_time = datetime.strptime(data['buy_time'], "%Y-%m-%d").date()
        except ValueError:
            return JsonResponse({"status": "wrong_date_format"})

        customer_id = data['customer']
        try:
            customer = Customer.objects.get(id=customer_id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "customer_not_found"})

        total_price = float(data['total_price'])

        purchase = Purchase.objects.create(buy_time=buy_time, customer=customer, total_price=total_price)
        purchase.items.set(items)
        purchase.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return PurchaseView.get_single(request, id)
        if request.method == "DELETE":
            return PurchaseView.delete(request, id)
        if request.method == "PATCH":
            return PurchaseView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "purchase_not_found"})
        return data_status(purchase_serializer(purchase))

    @staticmethod
    def delete(request, id):
        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "purchase_not_found"})

        purchase.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)

        try:
            purchase = Purchase.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "purchase_not_found"})

        if "items" in data:
            items_ids = data['items']
            items = []
            for item_id in items_ids:
                try:
                    item = Item.objects.get(id=item_id)
                    items.append(item)
                except ObjectDoesNotExist:
                    return JsonResponse({"status": "item_not_found"})
            purchase.items.set(items)

        if "buy_date" in data:
            try:
                buy_time = datetime.strptime(data['buy_time'], "%Y-%m-%d").date()
            except ValueError:
                return JsonResponse({"status": "wrong_date_format"})

            purchase.buy_time = buy_time

        if "customer" in data:
            customer_id = data['customer']
            try:
                customer = Customer.objects.get(id=customer_id)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "customer_not_found"})

            purchase.customer = customer

        if "total_price" in data:
            total_price = data['total_price']
            purchase.total_price = total_price

        purchase.save()
        return ok_status()
