from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed

from ..shop.models.customer_model import Customer
from ..serializers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')
