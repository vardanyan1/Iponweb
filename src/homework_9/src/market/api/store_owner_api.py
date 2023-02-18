import json
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from django.contrib.auth.models import User

from ..shop.models.store_owner_model import StoreOwner
from ..tools.sending_tools import data_status, ok_status
from ..serializers.store_owner_serializer import owner_serializer


class StoreOwnerView(View):
    @staticmethod
    def get(request):
        store_owners = StoreOwner.objects.all()
        data = []
        for owner in store_owners:
            data.append(owner_serializer(owner))

        return data_status(data=data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        username = data['username']
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "user_not_found"})
        store_owner = StoreOwner.objects.create(user=user)

        store_owner.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreOwnerView.get_single(request, id)
        if request.method == "DELETE":
            return StoreOwnerView.delete(request, id)
        if request.method == "PATCH":
            return StoreOwnerView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "obj_not_found"})
        return data_status(owner_serializer(owner))

    @staticmethod
    def delete(request, id):
        try:
            owner = StoreOwner.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "obj_not_found"})

        owner.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        if "username" in data:
            username = data['username']
            try:
                new_owner = User.objects.get(username=username)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "new_user_not_found"})

            try:
                owner = StoreOwner.objects.get(id=id)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "obj_not_found"})

            owner.user = new_owner
            owner.save()

        return ok_status()
