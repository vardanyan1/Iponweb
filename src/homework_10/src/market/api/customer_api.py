from rest_framework import viewsets
from ..shop.models.customer_model import Customer
from ..serializers.serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
