import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.generic import View
from django.contrib.auth.models import User
from ..shop.models.customer_model import Customer
from ..tools.sending_tools import data_status, ok_status
from ..serializers.customer_serializer import customer_serializer


class CustomerView(View):
    @staticmethod
    def get(request):
        customers = Customer.objects.all()
        data = []
        for customer in customers:
            data.append(customer_serializer(customer))

        return data_status(data=data)

    @staticmethod
    def post(request):
        data = json.loads(request.body)
        user_id = data['user']
        try:
            user = User.objects.get(id=user_id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "user_not_found"})

        customer = Customer.objects.create(user=user)

        customer.save()
        return ok_status()

    @staticmethod
    def check_view(request, id):
        if request.method == "GET":
            return CustomerView.get_single(request, id)
        if request.method == "DELETE":
            return CustomerView.delete(request, id)
        if request.method == "PATCH":
            return CustomerView.edit(request, id)

    @staticmethod
    def get_single(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "customer_not_found"})
        return data_status(customer_serializer(customer))

    @staticmethod
    def delete(request, id):
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "customer_not_found"})

        customer.delete()
        return ok_status()

    @staticmethod
    def edit(request, id):
        data = json.loads(request.body)
        try:
            customer = Customer.objects.get(id=id)
        except ObjectDoesNotExist:
            return JsonResponse({"status": "customer_not_found"})

        if "user" in data:
            user_id = data['user']
            try:
                user = User.objects.get(username=user_id)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "user_not_found"})

            customer.user = user
            customer.save()

        return ok_status()
