import json
from django.views.generic import View
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from ..shop.models.store_model import Store
from ..shop.models.store_owner_model import StoreOwner
from ..shop.models.store_category_model import StoreCategory
from ..tools.sending_tools import data_status, ok_status
from ..serializers.store_serializer import store_serializer


class StoreView(View):
    @staticmethod
    def get(request):
        stores = Store.objects.all()
        data = []
        for store in stores:
            data.append(store_serializer(store))

        return data_status(data=data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        name = data['name']
        owner_id = data['owner']
        try:
            owner = StoreOwner.objects.get(id=owner_id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "owner_not_found"})

        category_id = data['store_category']
        try:
            store_category = StoreCategory.objects.get(id=category_id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "category_not_found"})

        store = Store.objects.create(name=name, owner=owner, store_category=store_category)

        store.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreView.get_single(request, id)
        if request.method == "DELETE":
            return StoreView.delete(request, id)
        if request.method == "PATCH":
            return StoreView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "store_not_found"})
        return data_status(store_serializer(store))

    @staticmethod
    def delete(request, id):
        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "store_not_found"})

        store.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)

        try:
            store = Store.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "store_not_found"})

        if "name" in data:
            name = data['name']
            store.name = name

        if "owner" in data:
            owner_id = data['owner']
            try:
                owner = StoreOwner.objects.get(id=owner_id)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "owner_not_found"})

            store.owner = owner

        if "store_category" in data:
            store_category_id = data["store_category"]
            try:
                new_category = StoreCategory.objects.get(id=store_category_id)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "category_not_found"})

            store.store_category = new_category

        store.save()
        return ok_status()
