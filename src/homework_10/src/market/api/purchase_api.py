from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response

from ..shop.models.customer_model import Customer
from ..shop.models.item_model import Item
from ..shop.models.purchase_model import Purchase
from ..serializers.serializers import PurchaseSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

    def create(self, request, *args, **kwargs):
        item_ids = request.data.get('items', [])
        customer_id = request.data.get('customer')

        items = Item.objects.filter(id__in=item_ids)
        customer = Customer.objects.get(id=customer_id)

        total_price = sum(item.price for item in items)
        purchase = Purchase.objects.create(customer=customer, total_price=total_price, buy_time=timezone.now().date())
        purchase.items.set(items)

        serializer = self.get_serializer(purchase)
        return Response(serializer.data)
