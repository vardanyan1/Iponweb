import json
from django.views.generic import View
from ..shop.models.store_category_model import StoreCategory
from ..tools.sending_tools import data_status, ok_status
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse
from ..serializers.store_category_serializer import store_category_serializer


class StoreCategoryView(View):
    @staticmethod
    def get(request):
        categories = StoreCategory.objects.all()
        data = []
        for category in categories:
            data.append(store_category_serializer(category))

        return data_status(data=data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        category = StoreCategory.objects.create(
            name=data['name']
        )
        category.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return StoreCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return StoreCategoryView.delete(request, id)
        if request.method == "PATCH":
            return StoreCategoryView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "obj_not_found"})
        return data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "obj_not_found"})

        category.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = StoreCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data['name']
        category.save()
        return ok_status()
