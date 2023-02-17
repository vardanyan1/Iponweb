import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from ..tools.sending_tools import data_status, ok_status
from django.views.generic import View
from ..shop.models.items_category_model import ItemsCategory


class ItemsCategoryView(View):
    @staticmethod
    def get(request):
        categories = ItemsCategory.objects.all()
        data = []
        for category in categories:
            data.append({"name": category.name, "id": category.id})

        return data_status(data=data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        category = ItemsCategory.objects.create(
            name=data['name']
        )
        category.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return ItemsCategoryView.get_single(request, id)
        if request.method == "DELETE":
            return ItemsCategoryView.delete(request, id)
        if request.method == "PATCH":
            return ItemsCategoryView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            category = ItemsCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        return data_status({"id": category.id, "name": category.name})

    @staticmethod
    def delete(request, id):
        try:
            category = ItemsCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})

        category.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            category = ItemsCategory.objects.get(id=id)
        except ObjectDoesNotExist:
            return HttpResponse({"status": "obj_not_found"})
        if "name" in data:
            category.name = data['name']
        category.save()
        return ok_status()
