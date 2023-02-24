from rest_framework import viewsets
from ..shop.models.purchase_model import Purchase
from ..serializers.serializers import PurchaseSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
