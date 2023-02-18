import json
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
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
        owner_name = data['owner']
        try:
            user = User.objects.get(username=owner_name)
            owner = StoreOwner.objects.get(user=user)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "owner_not_found"})

        category_name = data['store_category']
        try:
            store_category = StoreCategory.objects.get(name=category_name)
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
        if "name" in data:
            name = data['name']
            try:
                store = Store.objects.get(id=id)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "store_not_found"})
            store.name = name
            store.save()

        if "owner" in data:
            new_owner_name = data['owner']
            try:
                new_owner_user = User.objects.get(username=new_owner_name)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "new_user_not_found"})

            try:
                new_owner = StoreOwner.objects.get(user=new_owner_user)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "new_owner_not_found"})

            try:
                store = Store.objects.get(id=id)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "store_not_found"})

            store.owner = new_owner
            store.save()

        if "store_category" in data:
            store_category = data["store_category"]

            try:
                store = Store.objects.get(id=id)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "store_not_found"})

            try:
                new_category = StoreCategory.objects.get(name=store_category)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "store_not_found"})
            store.store_category = new_category
            store.save()
        return ok_status()
